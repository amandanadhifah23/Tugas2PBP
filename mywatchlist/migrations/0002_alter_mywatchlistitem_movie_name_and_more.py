# Generated by Django 4.1 on 2022-09-22 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='movie_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='movie_review',
            field=models.TextField(),
        ),
    ]
