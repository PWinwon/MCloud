from django.db import models
from django.conf import settings

from movies.models import Movie
# Create your models here.

class Review(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_to_review')
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_to_review')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    title = models.CharField(max_length=50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = models.TextField()
