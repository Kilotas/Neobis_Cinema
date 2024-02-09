from django.db import models
from hall.models import Hall
from datetime import datetime

class MovieFormat(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Киноформат"

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class AgeLimit(models.Model):
    label = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.label

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    is_active = models.BooleanField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    age_limit = models.ForeignKey(AgeLimit, on_delete=models.CASCADE)
    date_start = models.DateField(default=None)
    date_end = models.DateField(default=None)
    movie_format = models.ForeignKey(MovieFormat, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Cinema(models.Model):
    title = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Кинотеатр"





class ShowTimes(models.Model):
    start_sessions = models.TimeField()
    end_sessions = models.TimeField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.start_sessions} - {self.end_session} {self.movie}"

    class Meta:
        verbose_name = "Сеансы"



#class ShowTime(models.Model):


