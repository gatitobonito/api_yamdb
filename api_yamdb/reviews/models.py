from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator


class Category(models.Model):
    SLUG_VALIDATOR = RegexValidator(r'^[-a-zA-Z0-9_]+$')
    name = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[SLUG_VALIDATOR]
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    SLUG_VALIDATOR = RegexValidator(r'^[-a-zA-Z0-9_]+$')
    name = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[SLUG_VALIDATOR]
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        validators=[
            MaxValueValidator(
                datetime.now().year, message='год выпуска не может быть больше'
                                             ' текущего')]
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='category',
    )
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} {self.genre}'
