# Generated by Django 3.1.7 on 2021-04-08 20:16

import apps.movies.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
                ('poster', imagekit.models.fields.ProcessedImageField(null=True, upload_to=apps.movies.helpers.upload_to_movie_image_directory)),
                ('imdb_rating', models.FloatField(blank=True, default=None, null=True)),
                ('rating', models.FloatField(blank=True, default=None, null=True)),
                ('slug', models.SlugField(default=None, unique=True)),
                ('genres', models.ManyToManyField(related_name='genres_of_movies', to='movies.Genre')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rating',
            },
        ),
    ]