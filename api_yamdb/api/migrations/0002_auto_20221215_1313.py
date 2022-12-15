# Generated by Django 3.2 on 2022-12-15 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='review',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='title',
            name='category',
        ),
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='titlegenre',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='titlegenre',
            name='title',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.DeleteModel(
            name='TitleGenre',
        ),
    ]
