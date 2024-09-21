from rest_framework.serializers import ModelSerializer

from apps.books.models import Book, Author, Genre


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        

class AuthorSerizalizer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        

class GenreSerizalizer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'