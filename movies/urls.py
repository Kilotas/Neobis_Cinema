from django.urls import path, include
from .views import CinemaViewSet, MovieFormatViewSet, MovieViewSet, ShowtimesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cinemas', CinemaViewSet, basename='cinema')
router.register(r'movie-formats', MovieFormatViewSet, basename='movie-format')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'showtimes', ShowtimesViewSet, basename='showtime')

urlpatterns = router.urls




