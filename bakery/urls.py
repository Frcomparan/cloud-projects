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
  path('bakery/categories', categories, name="categories-show"),
  path('bakery/categories/new', categories_new, name="categories-create"),
  path('bakery/categories/<int:id>/delete', categories_delete,name='categories-detail'),
  path('bakery/categories/<int:id>/edit', categories_edit,name='categories-edit'),
  path('bakery/cakes', cakes, name="cakes-show"),
  path('bakery/cakes/new', cakes_new, name="cakes-create"),
  path('bakery/cakes/<int:id>/delete', cakes_delete,name='cakes-detail'),
  path('bakery/cakes/<int:id>/edit', cakes_edit,name='cakes-edit'),
  path('bakery/orders', orders, name="orders-show"),
  path('bakery/orders/new', orders_new, name="orders-create"),
  path('bakery/orders/<int:id>/delete', orders_delete,name='orders-detail'),
  path('bakery/orders/<int:id>/edit', orders_edit,name='orders-edit'),
]