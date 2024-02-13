"""
URL configuration for NeobisCinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.views import UserViewSet
from drf_yasg.views import get_schema_view
router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="user")

schema_view = get_schema_view()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")), # Изменение пути для пользователей
    path("hall/", include("hall.urls")), # изменение путей для зала
    path("movies/", include("movies.urls")),
    path("orders/", include("orders.urls")),
    path("api/schema", SpectacularAPIView.as_view(), name='schema'),
    path("api/docs", SpectacularSwaggerView.as_view(url_name='schema'), name='docs')
]


