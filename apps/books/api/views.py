from rest_framework import viewsets

from .serializers import BookSerializer, AuthorSerizalizer, GenreSerizalizer
from apps.books.models import Book, Author, Genre


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerizalizer
    
    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerizalizer