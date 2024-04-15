from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from .models import PostCategory, User


# @receiver(m2m_changed, sender=PostCategory)
# def post_created(instance, **kwargs):
    # if kwargs['action'] != 'post_add':
    #     return
    #
    # emails = User.objects.filter(
    #     subscriptions__category__in=instance.category.all()
    # ).values_list('email', flat=True)
    #
    # subject = f'Новая публикация в категории {instance.category}'
    #
    # text_content = (
    #     f'Заголовок: {instance.title}\n'
    #     f'Содержание: {instance.text}\n'
    #     f'Ссылка на пост: {instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Заголовок: {instance.title}<br>'
    #     f'Содержание: {instance.text}<br><br>'
    #     f'<a href="http://127.0.0.1:8000/{instance.get_absolute_url()}">Ссылка на пост</a>'
    # )
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, 'text/html')
    #     msg.send()
