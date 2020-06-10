from rest_framework.generics import ListAPIView

from book.models import Book
from .serializers import BookSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer