from rest_framework.serializers import ModelSerializer

from book.models import Book

class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
        'id',
        'author',
        'title',
        'desc',
        'state',
        'created_date',
        'img'
        ]

class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
        'id',
        'author',
        'title',
        'desc',
        'state',
        'created_date',
        'img'
        ]