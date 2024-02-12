from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .serializers import HallTypeSerializer, HallSerializer, SeatSerializer
from .models import HallType, Hall, Seat
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly


class HallTypeAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk=None):
        if pk is not None:
            hall_type = HallType.objects.get(pk=pk)
            serializer = HallTypeSerializer(hall_type)
            return Response(serializer.data)
        else:
            hall_type = HallType.objects.all()
            serializer = HallTypeSerializer(hall_type, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = HallTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hall_type = HallType.objects.get(pk=pk)
        hall_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.

class HallAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk=None):
        if pk is not None:
            hall = Hall.objects.get(pk=pk)
            serializer = HallSerializer(hall)
            return Response(serializer.data)
        else:
            hall = Hall.objects.all()
            serializer = HallSerializer(hall, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hall = Hall.objects.get(pk=pk)
        serializer = HallSerializer(hall, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hall = Hall.objects.get(pk=pk)
        hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SeatAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk=None):
        if pk is not None:
            seat = Seat.objects.get(pk=pk)
            serializer = SeatSerializer(seat)
            return Response(serializer.data)
        else:
            seat = Seat.objects.all()
            serializer = SeatSerializer(seat, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        seat = Seat.objects.get(pk=pk)
        serializer = SeatSerializer(seat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seat = Seat.objects.get(pk=pk)
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








