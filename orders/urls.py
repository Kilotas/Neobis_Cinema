from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomBookingViewSet, CustomOrderViewSet, CustomTicketViewSet

router = DefaultRouter()

router.register(r'bookings', CustomBookingViewSet, basename='booking')
router.register(r'orders', CustomOrderViewSet, basename='order')
router.register(r'tickets', CustomTicketViewSet, basename='ticket')

urlpatterns = router.urls


