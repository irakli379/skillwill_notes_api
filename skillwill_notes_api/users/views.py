from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.views import APIView


@api_view(['POST'])
def register(request):
    if request.user.is_authenticated:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return  Response(status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={"error":"One of the fields is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        return Response(status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)
