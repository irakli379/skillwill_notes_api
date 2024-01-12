from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class NoteCollectionView(APIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = request.user.notes.all()
        serializer = self.serializer_class(instance=notes, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)