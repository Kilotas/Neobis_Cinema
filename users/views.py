from django.http import Http404

from .models import User, PurchaseHistory, Feedback
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from .serializers import UserSerializer, PurchaseHistorySerializer, FeedbackSerializer
from .permissions import UserPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission, ]


class PurchaseHistoryListCreateAPIView(APIView):
    def get(self, request):
        queryset = PurchaseHistory.objects.all()
        serializer = PurchaseHistorySerializer(queryset, many=True) # many=True означает что нужно сериализовать несколько объектов
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseHistorySerializer(data=request.data) # создается экземпляр сериализатора
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseHistoryRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return PurchaseHistory.objects.get(pk=pk)
        except PurchaseHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        purchase_history = self.get_object(pk)
        serializer = PurchaseHistorySerializer(purchase_history)
        return Response(serializer.data)

    def put(self, request, pk):
        purchase_history = self.get_object(pk)
        serializer = PurchaseHistorySerializer(purchase_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        purchase_history = self.get_object(pk)
        purchase_history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FeedbackViewSet(ModelViewSet): # Представляет реализацию круд операций
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


