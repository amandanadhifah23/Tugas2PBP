from django.db import models

class MyWatchlistItem(models.Model):
    watched_movie = models.BooleanField()
    movie_name = models.TextField()
    movie_rating = models.IntegerField()
    movie_date = models.DateField()
    movie_review = models.TextField()
