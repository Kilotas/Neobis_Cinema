from django.shortcuts import render
from datetime import date
from rest_framework.viewsets import ModelViewSet
from hall.permissions import IsAdminOrReadOnly
from .models import Cinema, Movie, ShowTimes, MovieFormat
from .serializers import CinemaSerializer, MovieFormatSerializer, MovieSerializers, ShowtimeSerializer
from django.utils import timezone
from datetime import datetime
# Create your views here.
class MovieFormatViewSet(ModelViewSet):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class CinemaViewSet(ModelViewSet):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializers
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()

    def get_queryset(self):
        current_date = datetime.today().date()
        movies = Movie.objects.filter(date_start__gte=current_date, date_end__lte=current_date, is_active=True)
        return movies
 #
class ShowtimesViewSet(ModelViewSet):
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        current_datetime = datetime.now()

        movies = Movie.objects.filter(date_end__gte=current_datetime.date())
 #  Смотрим фильмы которые еще не начались
        current_showtimes = ShowTimes.objects.filter(
            start_sessions__gte=current_datetime,
            movie__in=movies
        )
        return current_showtimes



