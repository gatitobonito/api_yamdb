# Generated by Django 3.2 on 2022-12-15 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20221216_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='created',
            new_name='pub_date',
        ),
    ]