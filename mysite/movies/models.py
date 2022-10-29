from django.db import models

# Create your models here.

class MovieData (models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length = 200)
    genre = models.CharField(max_length=200, default = 'action')
    duration = models.FloatField()
    rating = models.FloatField()

    def __str__(self): #overriding string method shows name of the movie in the admin panel
        return self.name
