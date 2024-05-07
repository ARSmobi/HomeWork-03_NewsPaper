from django.core.management.base import BaseCommand, CommandError
from NewsPaper.news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаляет все новости и статьи, относящиеся к выбранной категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы уверены в том, что хотите удалить все посты в категории {options["category"]}?  yes/no ')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCES(f'Все новости и статьи в категории {options["category"]} удалены'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Категория не найдена'))
