from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from workoutApp.models import CustomUser
from workoutApp.serializers import CreateUserSerializer


# Create your views here.


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


