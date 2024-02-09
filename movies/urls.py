from django.urls import path, include
from .views import CinemaViewSet, MovieFormatViewSet, MovieViewSet, ShowtimesViewSet

urlpatterns = [
    path('cinemas/', CinemaViewSet.as_view({'get': 'list'}), name='cinema-list'),
    path('cinemas/<int:pk>/', CinemaViewSet.as_view({'get': 'retrieve'}), name='cinema-detail'),
    path('movie-formats/', MovieFormatViewSet.as_view({'get': 'list'}), name='movie-format-list'),
    path('movie-formats/<int:pk>/', MovieFormatViewSet.as_view({'get': 'retrieve'}), name='movie-format-detail'),
    path('movies/', MovieViewSet.as_view({'get': 'list'}), name='movie-list'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve'}), name='movie-detail'),
    path('showtimes/', ShowtimesViewSet.as_view({'get': 'list'}), name='showtime-list'),
    path('showtimes/<int:pk>/', ShowtimesViewSet.as_view({'get': 'retrieve'}), name='showtime-detail'),
]





