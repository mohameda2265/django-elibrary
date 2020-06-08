from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.view_all, name='view_all'),
    path('books/new/',views.create_book,name='create_book'),
    path('books/<int:pk>/',views.book_details,name='book_details'),
    path('books/<int:pk>/edit',views.edit_book,name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]