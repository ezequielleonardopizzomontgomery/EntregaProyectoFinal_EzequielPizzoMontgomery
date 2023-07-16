from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

def book_image_directory(instance, filename):
    # Define la ruta de almacenamiento de las imágenes de libros
    return f'book_images/{instance.titulo}/{filename}'

class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = RichTextField(null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen_del_libro = models.ImageField(upload_to=book_image_directory)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
