from django.shortcuts import render
from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from hall.permissions import IsAdminOrReadOnly
from .models import Cinema, Movie, ShowTimes, MovieFormat
from .serializers import CinemaSerializer, MovieFormatSerializer, MovieSerializers, ShowtimeSerializer
from django.utils import timezone
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

    def get_queryset(self):
        current_date = timezone.now().date()
        return Movie.objects.filter(date_start__lte=current_date, date_end__gte=current_date) #

class ShowtimesViewSet(ModelViewSet):
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        # Получаем текущую дату и время
        current_datetime = timezone.now()

        # Фильтруем фильмы, для получения тех, которые еще не закончились
        movies = Movie.objects.filter(date_end__gte=current_datetime.date())
        # Теперь фильтруем сеансы, чтобы получить сеансы которые еще не начались

        current_showtimes = ShowTimes.objects.filter(
            start_sessions__gte=current_datetime,
            movie__in=movies
        )

        return current_showtimes




