from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect


def categories(request):
  if request.method == 'POST':
    form = create_category(request.POST)
    if form.is_valid():

      form.save()
      return redirect('categories-show')
    else:
      return render(request, 'bakery/categories/create_category.html', { 'form':form })

  categories = Category.objects.all()
  template = 'bakery/categories/show_category.html'
  context = {
    'categories':categories,
  }

  return render(request, template, context)

def categories_new(request):
  form = create_category
  template = 'bakery/categories/create_category.html'
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
  template = 'bakery/categories/update_category.html'
  context = {
    'category':category,
    'form':form,
  }
  return render(request, template, context)

def categories_delete(request, id):
  category = Category.objects.get(id=id)
  category.delete()
  return redirect(reverse('categories-show'))

def cakes(request):
  if request.method == 'POST':
    form = create_cake(request.POST)
    if form.is_valid():

      form.save()
      return redirect('cakes-show')
    else:
      context = {
        'errors':form.errors,
        'categories': Category.objects.all()
      }
      return render(request, 'bakery/cakes/create_cake.html', context)

  cakes = Cake.objects.all()
  template = 'bakery/cakes/show_cake.html'
  context = {
    'cakes':cakes,
  }

  return render(request, template, context)

def cakes_new(request):
  categories = Category.objects.all()
  template = 'bakery/cakes/create_cake.html'
  context = {
    'categories': categories
  }

  return render(request, template, context)

def cakes_edit(request, id):
  cake = Cake.objects.get(id=id)
  if request.method=='POST':
      form = create_cake(request.POST or None, instance=cake)
      if form.is_valid():
        form.save()
        return redirect('cakes-show')
      else:
        context = {
          'cake': cake,
          'errors':form.errors,
          'categories': Category.objects.all()
        }
        return render(request, 'bakery/cakes/update_cake.html', context)
  
  template = 'bakery/cakes/update_cake.html'
  categories = Category.objects.all()
  context = {
    'cake':cake,
    'categories':categories
  }
  return render(request, template, context)

def cakes_delete(request, id):
  cake = Cake.objects.get(id=id)
  cake.delete()
  return redirect(reverse('cakes-show'))

def orders(request):
  if request.method == 'POST':
    order = Order.objects.create()
    cakes = request.POST.getlist("cake")
    quantities = request.POST.getlist("quantity")
    print(cakes, quantities,'\n\n\n\n\n\n\n\n\n\n')
    for cake, quantity in zip(cakes, quantities):
      form = create_order({ 'order':order, 'cake':cake, 'quantity':quantity })
      if form.is_valid():
        form.save()
      else:
        return render(request, 'bakery/orders/create_order.html', { 'errors': 'Occurrio un error al realizar la compra' })
    set_total_order(order)

    return redirect('orders-show')

  orders = Order.objects.all()
  template = 'bakery/orders/show_order.html'
  context = {
    'orders':orders,
  }

  return render(request, template, context)

def orders_new(request):
  cakes = Cake.objects.all()
  template = 'bakery/orders/create_order.html'
  context = {
    'cakes': cakes,
  }

  return render(request, template, context)

def orders_edit(request, id):
  orderItems = OrderItem.objects.filter(order=id)
  cakes = Cake.objects.all()
  template = 'bakery/orders/update_order.html'
  context = {
    'orderItems':orderItems,
    'cakes': cakes,
    'id':id,
  }

  if request.method=='POST':
    ids, cakes, quantities = get_update_date(request)
    orderItems.exclude(pk__in=ids).delete()
    for item_id, cake, quantity in zip(ids, cakes, quantities):
      orderItem = OrderItem.objects.get(id=item_id)
      form = create_order({'order':id, 'cake':cake, 'quantity':quantity } or None, instance=orderItem)
      if form.is_valid():
        form.save()
      else:
        context['errors'] = 'Ocurrio un error'
        return render(request, template, context)
        
    set_total_order(Order.objects.get(id=id))
    return redirect('orders-show')  

  return render(request, template, context)

def orders_delete(request, id):
  order = Order.objects.get(id=id)
  order.delete()
  return redirect(reverse('orders-show'))

# Helper methods
def get_update_date(request):
  ids = request.POST.getlist("id")
  cakes = request.POST.getlist("cake")
  quantities = request.POST.getlist("quantity")
  return ids, cakes, quantities

def set_total_order(order):
  order_items = OrderItem.objects.filter(order=order.id)
  total = 0
  for order_item in order_items:
    total += order_item.cake.price * order_item.quantity
  form = update_order({'total':total} or None, instance=order)
  if form.is_valid():
    form.save()