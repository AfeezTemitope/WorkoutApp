from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workoutApp.views import CustomUserViewSet

router = DefaultRouter()
router.register('register', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]