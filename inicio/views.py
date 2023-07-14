from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy
from .forms import BookForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class InicioView(View):
    def get(self, request):
        contexto = {
            'mensaje': ''
        }
        return render(request, 'inicio/inicio.html', contexto)

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'inicio/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'inicio/book_create.html'
    form_class = BookForm
    success_url = reverse_lazy('inicio:book_list')

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'inicio/book_update.html'
    form_class = BookForm
    success_url = reverse_lazy('inicio:book_list')
    
class BookDeleteView(LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'inicio/book_confirm_delete.html'
    success_url = reverse_lazy('inicio:book_list')
