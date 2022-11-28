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
  path('pizzarela/categories', categories, name="categories-show"),
  path('pizzarela/categories/new', categories_new, name="categories-create"),
  path('pizzarela/categories/<int:id>/delete', categories_delete,name='categories-detail'),
  path('pizzarela/categories/<int:id>/edit', categories_edit,name='categories-edit'),
  path('pizzarela/products', products, name="products-show"),
  path('pizzarela/products/new', products_new, name="products-create"),
  path('pizzarela/products/<int:id>/delete', products_delete,name='products-detail'),
  path('pizzarela/products/<int:id>/edit', products_edit,name='products-edit'),
  path('pizzarela/orders', orders, name="orders-show"),
  path('pizzarela/orders/new', orders_new, name="orders-create"),
  path('pizzarela/orders/<int:id>/delete', orders_delete,name='orders-detail'),
  path('pizzarela/orders/<int:id>/edit', orders_edit,name='orders-edit'),
]