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
  path('books', books, name="show"),
  path('books/new', books_new, name="books-create"),
  path('books/<int:id>/delete', books_delete,name='books-detail'),
  path('books/<int:id>/edit', books_edit,name='books-edit'),
]