from rest_framework.serializers import ModelSerializer

from .models import HallType, Hall, Seat

class HallSerializer(ModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'name', 'price']


class HallTypeSerializer(ModelSerializer):
    class Meta:
        model = HallType
        fields = ['id', 'name', 'price']

class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'hall', 'seat']




