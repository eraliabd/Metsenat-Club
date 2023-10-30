from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreate(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
