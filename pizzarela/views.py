from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def categories(request):
  if request.method == 'POST':
    form = create_category(request.POST)
    if form.is_valid():

      form.save()
      return redirect('categories-show')
    else:
      return render(request, 'categories/create_category.html', { 'form':form })

  categories = Category.objects.all()
  template = 'categories/show_category.html'
  context = {
    'categories':categories,
  }

  return render(request, template, context)

def categories_new(request):
  form = create_category
  template = 'categories/create_category.html'
  context = {
    'form':form,
  }

  return render(request, template, context)

def categories_edit(request, id):
  category = Category.objects.get(id=id)
  if request.method=='POST':
      form = create_category(request.POST or None, instance=category)
      if form.is_valid():
        form.save()
        return redirect('categories-show')
  
  form = create_category(instance=category)
  template = 'categories/update_category.html'
  context = {
    'category':category,
    'form':form,
  }
  return render(request, template, context)

def categories_delete(request, id):
  category = Category.objects.get(id=id)
  category.delete()
  return redirect(reverse('categories-show'))

def products(request):
  if request.method == 'POST':
    form = create_product(request.POST)
    if form.is_valid():

      form.save()
      return redirect('products-show')
    else:
      context = {
        'errors':form.errors,
        'categories': Category.objects.all()
      }
      return render(request, 'products/create_product.html', context)

  products = Product.objects.all()
  template = 'products/show_product.html'
  context = {
    'products':products,
  }

  return render(request, template, context)

def products_new(request):
  categories = Category.objects.all()
  template = 'products/create_product.html'
  context = {
    'categories': categories
  }

  return render(request, template, context)

def products_edit(request, id):
  product = Product.objects.get(id=id)
  if request.method=='POST':
      form = create_product(request.POST or None, instance=product)
      if form.is_valid():
        form.save()
        return redirect('products-show')
      else:
        context = {
          'product': product,
          'errors':form.errors,
          'categories': Category.objects.all()
        }
        return render(request, 'products/update_product.html', context)
  
  template = 'products/update_product.html'
  categories = Category.objects.all()
  context = {
    'product':product,
    'categories':categories
  }
  return render(request, template, context)

def products_delete(request, id):
  product = Product.objects.get(id=id)
  product.delete()
  return redirect(reverse('products-show'))

def orders(request):
  if request.method == 'POST':
    form = create_order(request.POST)
    if form.is_valid():

      form.save()
      return redirect('orders-show')
    else:
      context = {
        'errors':form.errors,
        'categories': Category.objects.all()
      }
      return render(request, 'orders/create_order.html', context)

  orders = Order.objects.all()
  template = 'orders/show_order.html'
  context = {
    'orders':orders,
  }

  return render(request, template, context)

def orders_new(request):
  products = Product.objects.all()
  template = 'orders/create_order.html'
  context = {
    'products': products
  }

  return render(request, template, context)

def orders_edit(request, id):
  order = Order.objects.get(id=id)
  if request.method=='POST':
      form = create_order(request.POST or None, instance=order)
      if form.is_valid():
        form.save()
        return redirect('orders-show')
      else:
        context = {
          'order': order,
          'errors':form.errors,
          'categories': Category.objects.all()
        }
        return render(request, 'orders/update_order.html', context)
  
  template = 'orders/update_order.html'
  categories = Category.objects.all()
  context = {
    'order':order,
    'categories':categories
  }
  return render(request, template, context)

def orders_delete(request, id):
  order = Order.objects.get(id=id)
  order.delete()
  return redirect(reverse('orders-show'))