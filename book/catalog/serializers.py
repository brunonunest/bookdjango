from rest_framework import serializers
from . models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'name', 'author', 'category', 'review', 'read')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'email', 'password']
