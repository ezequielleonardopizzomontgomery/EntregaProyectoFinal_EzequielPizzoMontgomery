from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['titulo', 'autor', 'descripcion', 'precio', 'vendedor', 'imagen_del_libro']
