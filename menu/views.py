from django.shortcuts import render, redirect
from .models import Order

def home(request):
    return render(request, 'menu/home.html')

def order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        item = request.POST['item']
        quantity = request.POST.get('quantity', 1)
        
        Order.objects.create(
            customer_name=customer_name,
            item=item,
            quantity=quantity
        )
        return redirect('home')
    
    return render(request, 'menu/order.html')