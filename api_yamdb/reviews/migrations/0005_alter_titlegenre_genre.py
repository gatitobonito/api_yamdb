# Generated by Django 3.2 on 2022-12-14 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_merge_20221214_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlegenre',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.genre'),
        ),
    ]