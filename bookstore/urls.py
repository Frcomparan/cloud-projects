from django.contrib import admin
from django.urls import path
from .views import*
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from .views import *


urlpatterns = [
  path('books', books, name="books-show"),
  path('books/new', books_new, name="books-create"),
  path('books/<int:id>/delete', books_delete,name='books-detail'),
  path('books/<int:id>/edit', books_edit,name='books-edit'),
  path('borrows', borrows, name="borrows-show"),
  path('borrows/new', borrows_new, name="borrows-create"),
  path('borrows/<int:id>/delete', borrows_delete,name='borrows-detail'),
  path('borrows/<int:id>/edit', borrows_edit,name='borrows-edit'),
]