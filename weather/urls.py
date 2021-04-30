from django.urls import path, include
from weather import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('description', views.WeatherDiscription)

urlpatterns = [
    path('', include(router.urls))
]