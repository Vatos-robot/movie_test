from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='films')
    @property
    def average_rating(self):
        agg = self.reviews.aggregate(avg=Avg('rating'))
        return agg['avg'] or 0.0

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.movie.title} – {self.rating}"

