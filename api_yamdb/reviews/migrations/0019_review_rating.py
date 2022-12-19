# Generated by Django 3.2 on 2022-12-19 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0018_alter_review_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]