# Generated by Django 3.2 on 2022-12-16 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_rename_title_review_title_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='review_id',
        ),
    ]
