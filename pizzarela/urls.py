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
  path('categories', categories, name="categories-show"),
  path('categories/new', categories_new, name="categories-create"),
  path('categories/<int:id>/delete', categories_delete,name='categories-detail'),
  path('categories/<int:id>/edit', categories_edit,name='categories-edit'),
  path('products', products, name="products-show"),
  path('products/new', products_new, name="products-create"),
  path('products/<int:id>/delete', products_delete,name='products-detail'),
  path('products/<int:id>/edit', products_edit,name='products-edit'),
]