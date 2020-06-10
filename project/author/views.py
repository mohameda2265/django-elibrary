from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Author
from book.models import Book
from .forms import AuthorForm
from .filters import AuthorFilter
from django.http import HttpResponse

def view_all(request):
    author = Author.objects.all()
    myFilter = AuthorFilter(request.GET,queryset=author)
    author = myFilter.qs
    context = {"author":author,"myFilter":myFilter}
    return render(request, 'author/view_all.html', context)


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid:
            author = form.save(commit=False)
            author = form.save()
            return redirect('/')
    else:
        form = AuthorForm()
        return render(request,'author/create_author.html',{'form':form})

def edit_author(request,pk):
    author = get_object_or_404(Author,pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST,instance=author)
        if form.is_valid:
            author = form.save(commit=False)
            author = form.save()
            return redirect('/')
    else:
        form = AuthorForm(instance=author)
        return render(request,'author/edit_author.html',{'form':form})

def author_details(request,pk):
    author = get_object_or_404(Author,pk=pk)
    books = Book.objects.filter(author__id=pk)
    return render(request, 'author/author_details.html', {"author":author,"books":books})

def delete_author(request,pk):
    author = get_object_or_404(Author,pk=pk)
    author.delete()
    return redirect('view_all')
