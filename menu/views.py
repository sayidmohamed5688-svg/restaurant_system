
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, MenuItem

def home(request):
    menu_items = MenuItem.objects.filter(available=True)
    return render(request, 'menu/home.html', {'menu_items': menu_items})

def order(request):
    menu_items = MenuItem.objects.filter(available=True)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '')
        item = request.POST.get('item', '')
        quantity = request.POST.get('quantity', 1)
        new_order = Order.objects.create(
            customer_name=customer_name,
            item=item,
            quantity=quantity
        )
        return redirect('receipt', pk=new_order.pk)
    return render(request, 'menu/order.html', {'menu_items': menu_items})
@login_required
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'menu/all_orders.html', {'orders': orders})

def receipt(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'menu/receipt.html', {'order': order})

@login_required
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('all_orders')

@login_required
def edit_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.customer_name = request.POST.get('customer_name', '')
        order.item = request.POST.get('item', '')
        order.quantity = request.POST.get('quantity', 1)
        order.save()
        return redirect('all_orders')
    return render(request, 'menu/edit_order.html', {'order': order})

def search(request):
    query = request.GET.get('q', '')
    results = Order.objects.filter(customer_name__icontains=query)
    return render(request, 'menu/search.html', {
        'results': results,
        'query': query
    })