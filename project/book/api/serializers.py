from rest_framework.serializers import ModelSerializer

from book.models import Book

class BookSerializer(ModelSerializer):
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