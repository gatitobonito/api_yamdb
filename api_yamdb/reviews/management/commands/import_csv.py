from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category, Genre, Title, TitleGenre

ERROR_MESSAGE = """Уничтожьте базу данных и заново сделайте миграции"""


class Command(BaseCommand):
    help = "Загружает данные из genre.csv"

    def handle(self, *args, **options):
        if Genre.objects.exists():
            print('существующие данные')
            print(ERROR_MESSAGE)
            return
        print("Загрузка данных")

        for row in DictReader(
                open('./static/data/genre.csv')
        ):
            genre = Genre(
                name=row['name'],
                slug=row['slug']
            )
            genre.save()


class Command(BaseCommand):
    help = "Загружает данные из category.csv"

    def handle(self, *args, **options):
        if Category.objects.exists():
            print('существующие данные.')
            print(ERROR_MESSAGE)
            return
        print("Загрузка данных")

        for row in DictReader(
                open('./static/data/category.csv')
        ):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()


class Command(BaseCommand):
    help = "Загружает данные из title.csv"

    def handle(self, *args, **options):
        if Title.objects.exists():
            print('существующие данные.')
            print(ERROR_MESSAGE)
            return
        print("Загрузка данных")

        for row in DictReader(
                open('./static/data/titles.csv')
        ):
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category']
            )
            title.save()


class Command(BaseCommand):
    help = "Загружает данные из genre_title.csv"

    def handle(self, *args, **options):
        if TitleGenre.objects.exists():
            print('существующие данные.')
            print(ERROR_MESSAGE)
            return
        print("Загрузка данных")

        for row in DictReader(
                open('./static/data/genre_title.csv')
        ):
            titlegenre = TitleGenre(
                id=row['id'],
                title_id=row['title_id'],
                genre_id=row['genre_id']
            )
            titlegenre.save()
