from django.db import models



class Director(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=222)
    description = models.TextField(max_length=222, blank=True)
    duration = models.DurationField(max_length=222)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(null=True,blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')