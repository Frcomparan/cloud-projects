from multiprocessing.sharedctypes import Value
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CategorySelect(forms.Select):
  def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
    option = super().create_option(name, value, label, selected, index, subindex, attrs)
    if value:
      option['name'] = value.instance.name
    return option

class create_category(forms.ModelForm):
  class Meta:
    model = Category
    fields= ['id','name','description']

class create_cake(forms.ModelForm):
  class Meta:
    model = Cake
    fields= ['id','name','price', 'category']

class create_order(forms.ModelForm):
  class Meta:
    model = OrderItem
    fields= ['id','quantity','cake','order']

class update_order(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['id', 'total']