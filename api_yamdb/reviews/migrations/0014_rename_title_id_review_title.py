# Generated by Django 3.2 on 2022-12-19 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_rename_review_comment_review_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title_id',
            new_name='title',
        ),
    ]
