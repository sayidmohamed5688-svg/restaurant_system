from django.shortcuts import render, redirect
from .models import Order

def home(request):
    return render(request, 'menu/home.html')

def order(request):
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
    
    return render(request, 'menu/order.html')

def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'menu/all_orders.html', {'orders': orders})

def receipt(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'menu/receipt.html', {'order': order})

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('all_orders')



def edit_order(request, pk):
    order = Order.objects.get(pk=pk)
    
    if request.method == 'POST':
        order.customer_name = request.POST.get('customer_name', '')
        order.item = request.POST.get('item', '')
        order.quantity = request.POST.get('quantity', 1)
        order.save()
        return redirect('all_orders')
    
    return render(request, 'menu/edit_order.html', {'order': order})