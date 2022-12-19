# Generated by Django 3.2 on 2022-12-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_rename_title_id_review_title'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_title_author'),
        ),
    ]
