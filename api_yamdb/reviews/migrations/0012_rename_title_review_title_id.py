# Generated by Django 3.2 on 2022-12-16 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20221217_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='title_id',
        ),
    ]
