from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FeedbackViewSet, CustomClubCardViewSet

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Регистрируем представления в роутере
router.register(r'users', UserViewSet, basename='user')

router.register(r'feedbacks', FeedbackViewSet, basename='feedback')
router.register(r'clubcards', CustomClubCardViewSet, basename='clubcard')

# Получаем маршруты URL из роутера
urlpatterns = router.urls




