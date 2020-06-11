from rest_framework.generics import ListAPIView, RetrieveAPIView

from book.models import Book
from .serializers import BookListSerializer, BookDetailSerializer

# get all objects from book model 
# and serialize it into json object
class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

# pass the pk or id to this method and it implicitly call 'RetrieveAPIView',
# and match the data to the queryset depends on passed pk
class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    # if we wanna to get data with anything else not the id
    # we can set the new value here
    # lookup_field = 'title'
    # and pass the param to url path like that 'route'
    # lookup_url_kwarg = 'tit'