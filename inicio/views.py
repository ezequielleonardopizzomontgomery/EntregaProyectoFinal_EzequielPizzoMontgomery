from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def inicio(request):
    return render(request, 'inicio/inicio.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'inicio/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'inicio/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio/book_list')
    else:
        form = BookForm()
    return render(request, 'inicio/book_create.html', {'form': form})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('inicio/book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'inicio/book_update.html', {'form': form, 'book': book})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('inicio/book_list')
    return render(request, 'inicio/book_delete.html', {'book': book})

