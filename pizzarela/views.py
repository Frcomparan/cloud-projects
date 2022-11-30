from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def home(request):
  template = 'pizzarela_home.html'
  return render(request, template)

def categories(request):
  if request.method == 'POST':
    form = create_category(request.POST)
    if form.is_valid():

      form.save()
      return redirect('pizzarela-categories-show')
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
        return redirect('pizzarela-categories-show')
  
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
  return redirect(reverse('pizzarela-categories-show'))

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
    order = Order.objects.create()
    products = request.POST.getlist("product")
    quantities = request.POST.getlist("quantity")
    for product, quantity in zip(products, quantities):
      form = create_order({ 'order':order, 'product':product, 'quantity':quantity })
      if form.is_valid():
        form.save()
      else:
        return render(request, 'orders/create_order.html', { 'errors': 'Occurrio un error al realizar la compra' })
    set_total_order(order)

    return redirect('pizzarela-orders-show')

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
    'products': products,
  }

  return render(request, template, context)

def orders_edit(request, id):
  orderItems = OrderItem.objects.filter(order=id)
  products = Product.objects.all()
  template = 'orders/update_order.html'
  context = {
    'orderItems':orderItems,
    'products': products,
    'id':id,
  }

  if request.method=='POST':
    ids, products, quantities = get_update_date(request)
    orderItems.exclude(pk__in=ids).delete()
    for item_id, product, quantity in zip(ids, products, quantities):
      orderItem = OrderItem.objects.get(id=item_id)
      form = create_order({'order':id, 'product':product, 'quantity':quantity } or None, instance=orderItem)
      if form.is_valid():
        form.save()
      else:
        context['errors'] = 'Ocurrio un error'
        return render(request, template, context)
        
    set_total_order(Order.objects.get(id=id))
    return redirect('pizzarela-orders-show')  

  return render(request, template, context)

def orders_delete(request, id):
  order = Order.objects.get(id=id)
  order.delete()
  return redirect(reverse('pizzarela-orders-show'))

# Helper methods
def get_update_date(request):
  ids = request.POST.getlist("id")
  products = request.POST.getlist("product")
  quantities = request.POST.getlist("quantity")
  return ids, products, quantities

def set_total_order(order):
  order_items = OrderItem.objects.filter(order=order.id)
  total = 0
  for order_item in order_items:
    total += order_item.product.price * order_item.quantity
  form = update_order({'total':total} or None, instance=order)
  if form.is_valid():
    form.save()