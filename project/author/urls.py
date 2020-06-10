from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'author'

urlpatterns = [
    path('authors/', views.view_all, name='view_all'),
    path('authors/new/',views.create_author,name='create_author'),
    path('authors/<int:pk>/',views.author_details,name='author_details'),
    path('authors/<int:pk>/edit',views.edit_author,name='edit_author'),
    path('authors/<int:pk>/delete', views.delete_author, name='delete_author'),
]
