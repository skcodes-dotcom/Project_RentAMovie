from django.db import models
from django.utils import timezone


# Each Genre will have a Movie. Create a relationship between the Genre class and the Movie class.
# If you delete a Genre all the Movies associated with it should be deleted.
# Line 12: In the Django Admin, display the name of the Genre.

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


