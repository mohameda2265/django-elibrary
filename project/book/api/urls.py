from django.urls import path
# from django.conf.urls import url
from . import views
app_name = 'books-api'
urlpatterns = [
    path('', views.BookListAPIView.as_view(), name='list'),
    # path('admin/', views.admin, name='admin'),
    # path('books/new/',views.create_book,name='create_book'),
    # path('books/<int:pk>/',views.book_details,name='book_details'),
    # path('books/<int:pk>/edit/',views.edit_book,name='edit_book'),
    # path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]

