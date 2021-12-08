from django.db import models
from django.conf import settings
from django_random_queryset import RandomManager

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Keyword(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    release_date = models.DateTimeField()
    adult = models.BooleanField()

    genres = models.ManyToManyField(Genre, related_name='movies')
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_like_movies')

    movie_keywords = models.ManyToManyField(Keyword, related_name='keyword_movies')

    objects = RandomManager()

