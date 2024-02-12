from django.http import Http404

from .models import User, Feedback, ClubCard
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from .serializers import UserSerializer, FeedbackSerializer, ClubCardSerializer
from .permissions import UserPermission
from hall.permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission, ]

class CustomClubCardViewSet(ModelViewSet):
    serializer_class = ClubCardSerializer
    queryset = ClubCard.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class FeedbackViewSet(ModelViewSet): # Представляет реализацию круд операций
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


