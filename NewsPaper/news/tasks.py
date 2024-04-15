from celery import shared_task
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, User, Subscription


@shared_task  # рассылка для подписанных на категорию о постах за последнюю неделю
def latest_news():
    posts = Post.objects.filter(date_creation__gte=datetime.now()-timedelta(days=7))
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Subscription.objects.filter(
        category__in=categories).values_list('user__email', flat=True))

    html_content = render_to_string('daily_post.html',
                                    {'link': settings.SITE_URL,
                                     'posts': posts})
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task  # рассылка для подписанных на категорию при создании нового поста
def created_post_notification(pid):
    post = Post.objects.get(pk=pid)
    emails = User.objects.filter(
        subscriptions__category__in=post.category.all()
    ).values_list('email', flat=True)
    subject = f'Новая публикация в категории {post.category}'
    text_content = (
        f'Заголовок: {post.title}\n'
        f'Содержание: {post.text}\n'
        f'Ссылка на пост: {post.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок: {post.title}<br>'
        f'Содержание: {post.text}<br><br>'
        f'<a href="http://127.0.0.1:8000/{post.get_absolute_url()}">Ссылка на пост</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
