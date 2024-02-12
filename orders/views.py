from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Order, Ticket
from .serializers import BookingSerializer, OrderSerializer, TicketSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import ClubCard
# Create your views here.

class CustomTicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticated]

class CustomBookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

class CustomOrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_total_price(self, obj):
        tickets = Ticket.objects.filter(order_id=obj.id)
        total_price = sum(ticket.price for ticket in tickets)
        return total_price

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for order_data in data:
            order_id = order_data['id']
            order_obj = Order.objects.get(id=order_id)
            order_data['total_price'] = self.get_total_price(order_obj)
        return Response(data)



