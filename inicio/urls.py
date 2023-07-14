from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView ,BookCreateView , InicioView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


app_name = 'inicio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),
    path('listar_libros/', BookListView.as_view(), name='book_list'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

