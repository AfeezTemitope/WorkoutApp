from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from workoutApp.models import CustomUser
from workoutApp.serializers import CreateUserSerializer


# Create your views here.


class CustomUserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


class CustomAuthToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'detail': 'all field required'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'detail': 'invalid'},
                            status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access_token)
        })


