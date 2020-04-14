from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer


#General view to CRUD on book catalog
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
