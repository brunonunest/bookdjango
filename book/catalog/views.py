from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
