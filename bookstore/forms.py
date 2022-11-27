from multiprocessing.sharedctypes import Value
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class create_book(forms.ModelForm):
  class Meta:
    model = Book
    fields= ['id','title','description','author','release_date','pages']
    widgets = {
      'release_date': forms.DateInput(attrs={'type': 'date'})
    }

class create_borrow(forms.ModelForm):
  class Meta:
    model = Borrow
    fields= ['id','book_id']