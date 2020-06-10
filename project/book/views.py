from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Book
from .forms import BookForm
from .filters import BookFilter
from django.http import HttpResponse

def view_all(request):
    book = Book.objects.all()
    myFilter = BookFilter(request.GET,queryset=book)
    book = myFilter.qs
    context = {"book":book,"myFilter":myFilter}
    return render(request, 'book/view_all.html', context)


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST or None , request.FILES or None)
        if form.is_valid:
            book = form.save(commit=False)
            book = form.save()
            return redirect('/')
    else:
        form = BookForm()
        return render(request,'book/create_book.html',{'form':form})

def edit_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES or None, instance=book)
        if form.is_valid:
            book = form.save(commit=False)
            book = form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
        return render(request,'book/create_book.html',{'form':form})

def book_details(request,pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request, 'book/book_details.html', {"book":book})

def delete_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    book.delete()
    return redirect('view_all')

def admin(request):
    return redirect('admin')