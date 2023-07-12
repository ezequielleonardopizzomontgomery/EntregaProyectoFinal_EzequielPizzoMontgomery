from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

def book_image_directory(instance, filename):
    # Define la ruta de almacenamiento de las imágenes de libros
    return f'book_images/{instance.title}/{filename}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = RichTextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=book_image_directory)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

