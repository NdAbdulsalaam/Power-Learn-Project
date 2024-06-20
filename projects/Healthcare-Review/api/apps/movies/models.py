import uuid
from imagekit.models import ProcessedImageField

from django.db import models, transaction
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import F, Count, Q

from .helpers import (
    upload_to_actor_image_directory,
    upload_to_movie_image_directory,
)
from apps.common.model_loaders import (
    get_user_model,
    get_comment_model,
    get_rating_model,
)
from apps.accounts.models import User


class Genre(models.Model):
    name = models.CharField(
        max_length=settings.GENRE_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
    )

    class Meta:
        db_table = "genre"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=settings.MOVIE_TITLE_MAX_LENGTH)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    director = models.CharField(
        max_length=settings.MOVIE_DIRECTOR_MAX_LENGTH, blank=True, null=True
    )
    poster = models.TextField(blank=True, null=True)
    imdb_rating = models.FloatField(blank=True, null=True)
    rating_average = models.FloatField(blank=True, default=0)
    rating_count = models.IntegerField(blank=True, default=0)
    view_count = models.IntegerField(blank=True, default=0)
    slug = models.SlugField(
        max_length=settings.MOVIE_SLUG_MAX_LENGTH,
        db_index=True,
        unique=True,
        blank=False,
    )
    genres = models.ManyToManyField(Genre, related_name="movies_genres")

    class Meta:
        db_table = "movie"
        ordering = ["id"]

    def __str__(self):
        return self.title

    @property
    def genres_indexing(self):
        """Genres for indexing.

        Used in Elasticsearch indexing.
        """
        return [genre.name for genre in self.genres.all()]

    @classmethod
    def get_movie_with_slug(cls, movie_slug):
        with transaction.atomic():
            movie = cls.objects.select_for_update().get(slug=movie_slug)
            movie.view_count += 1
            movie.save()
        return movie

    def count_comments(self):
        Comment = get_comment_model()
        return Comment.count_comment_for_movie_with_id(self.pk)

    def get_rating_info(self):
        rating_info = Rating.get_rating_info_for_movie_with_id(self.pk)
        return rating_info

    @classmethod
    def update_movie_rating_info(cls, movie):
        new_rating_count = Rating.objects.filter(movie=movie).count()
        new_rating_average = (
            Rating.objects.filter(movie=movie)
            .aggregate(models.Avg("rating"))
            .get("rating__avg")
        )

        movie.rating_count = new_rating_count
        movie.rating_average = (
            round(new_rating_average, 1) if new_rating_average else 0
        )
        movie.save()


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="rates",
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rates",
        null=False,
        blank=False,
    )
    rating = models.FloatField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rating"

    @classmethod
    def get_rating_info_for_movie_with_id(cls, movie_id):
        n_1_star = cls.objects.filter(
            Q(rating__lt=2) & Q(movie=movie_id)
        ).count()
        n_2_star = cls.objects.filter(
            Q(rating__gte=2) & Q(rating__lt=3) & Q(movie=movie_id)
        ).count()
        n_3_star = cls.objects.filter(
            Q(rating__gte=3) & Q(rating__lt=4) & Q(movie=movie_id)
        ).count()
        n_4_star = cls.objects.filter(
            Q(rating__gte=4) & Q(rating__lt=5) & Q(movie=movie_id)
        ).count()
        n_5_star = cls.objects.filter(Q(rating=5) & Q(movie=movie_id)).count()
        return [n_1_star, n_2_star, n_3_star, n_4_star, n_5_star]

    @classmethod
    def get_with_id(cls, rating_id):
        return cls.objects.get(pk=rating_id)

    @classmethod
    def delete_with_id(cls, rating_id):
        rating = cls.objects.get(pk=rating_id)
        movie = Movie.objects.get(pk=rating.movie_id)

        rating.delete()
        Movie.update_movie_rating_info(movie)
        return True
