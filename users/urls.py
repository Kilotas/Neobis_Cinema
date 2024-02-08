
from django.urls import path
from .views import UserViewSet, PurchaseHistoryListCreateAPIView, PurchaseHistoryRetrieveUpdateDestroyAPIView, FeedbackViewSet

urlpatterns = [
    # URL-адреса для пользователей
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),

    # URL-адреса для списка покупок и их деталей
    path('purchasehistories/', PurchaseHistoryListCreateAPIView.as_view(), name='purchasehistory-list-create'),
    path('purchasehistories/<int:pk>/', PurchaseHistoryRetrieveUpdateDestroyAPIView.as_view(), name='purchasehistory-retrieve-update-destroy'),

    # URL-адреса для обратной связи (Feedback)
    path('feedbacks/', FeedbackViewSet.as_view({'get': 'list', 'post': 'create'}), name='feedback-list'),
    path('feedbacks/<int:pk>/', FeedbackViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='feedback-detail'),
]



