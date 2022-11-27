from django.shortcuts import render
from .models import Book
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def books(request):
  if request.method == 'POST':
    form = create(request.POST)
    if form.is_valid():

      form.save()
      return redirect('show')
    else:
      return render(request, 'create.html', { 'form':form })

  books = Book.objects.all()
  template = 'show.html'
  context = {
    'books':books,
  }

  return render(request, template, context)

def books_new(request):
  form = create
  template = 'create.html'
  context = {
    'form':form,
  }

  return render(request, template, context)

def books_edit(request, id):
  book = Book.objects.get(id=id)
  if request.method=='POST':
      form = create(request.POST or None, instance=book)
      if form.is_valid():
        form.save()
        return redirect('show')
  
  form = create(instance=book)
  template = 'update.html'
  context = {
    'book':book,
    'form':form,
  }
  return render(request, template, context)

def books_delete(request, id):
  book = Book.objects.get(id=id)
  book.delete()
  return redirect(reverse('show'))