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
    form = create_book(request.POST)
    if form.is_valid():

      form.save()
      return redirect('show')
    else:
      return render(request, 'create_book.html', { 'form':form })

  books = Book.objects.all()
  template = 'show_book.html'
  context = {
    'books':books,
  }

  return render(request, template, context)

def books_new(request):
  form = create_book
  template = 'create_book.html'
  context = {
    'form':form,
  }

  return render(request, template, context)

def books_edit(request, id):
  book = Book.objects.get(id=id)
  if request.method=='POST':
      form = create_book(request.POST or None, instance=book)
      if form.is_valid():
        form.save()
        return redirect('show')
  
  form = create_book(instance=book)
  template = 'update_book.html'
  context = {
    'book':book,
    'form':form,
  }
  return render(request, template, context)

def books_delete(request, id):
  book = Book.objects.get(id=id)
  book.delete()
  return redirect(reverse('show'))

def borrows(request):
  if request.method == 'POST':
    form = create_borrow(request.POST)
    if form.is_valid():

      form.save()
      return redirect('show')
    else:
      return render(request, 'create_borrow.html', { 'form':form })

  borrows = Borrow.objects.all()
  template = 'show_borrow.html'
  context = {
    'borrows':borrows,
  }

  return render(request, template, context)

def borrows_new(request):
  borrows_books = Borrow.objects.filter(is_returned=False)
  borrows_books_ids = [ book.book_id.id for book in borrows_books ]
  books = Book.objects.exclude(pk__in=borrows_books_ids)
  template = 'create_borrow.html'
  context = {
    'books':books,
  }

  return render(request, template, context)

def borrows_edit(request, id):
  borrow = Borrow.objects.get(id=id)
  if request.method=='POST':
      form = update_borrow(request.POST or None, instance=borrow)
      if form.is_valid():
        form.save()
        return redirect('show')
  
  form = update_borrow(instance=borrow)
  template = 'update_borrow.html'
  context = {
    'borrow':borrow,
    'form':form,
  }
  return render(request, template, context)

def borrows_delete(request, id):
  borrow = Borrow.objects.get(id=id)
  borrow.delete()
  return redirect(reverse('show'))