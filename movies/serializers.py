from rest_framework.serializers import ModelSerializer
from .models import Cinema, Movie, ShowTimes, MovieFormat


class CinemaSerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'title', 'phone_number', 'city', 'address', 'start_time', 'end_time']

class MovieFormatSerializer(ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = ['id', 'name', 'price']

class MovieSerializers(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'is_active', 'genre', 'age_limit']

class ShowtimeSerializer(ModelSerializer):
    class Meta:
        model = ShowTimes
        fields = ['id', 'start_sessions', 'end_sessions', 'cinema', 'movie', 'hall']


