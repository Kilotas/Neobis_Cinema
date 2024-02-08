from django.urls import path
from .views import HallTypeAPIView, HallAPIView, SeatAPIView
urlpatterns = [
    path('hall-types/', HallTypeAPIView.as_view(), name='hall-type-list'),
    path('hall-types/<int:pk>/', HallTypeAPIView.as_view(), name='hall-type-detail'),

    path('rooms/', HallAPIView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', HallAPIView.as_view(), name='room-detail'),

    path('seats/', SeatAPIView.as_view(), name='seat-list'),
    path('seats/<int:pk>/', SeatAPIView.as_view(), name='seat-detail'),

]