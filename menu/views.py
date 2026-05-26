from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, MenuItem, Category, Table, OrderItem


def home(request):
    categories = Category.objects.all()
    return render(request, 'menu/home.html', {'categories': categories})

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

def waiter_dashboard(request):
    from django.contrib.auth.models import User
    waiters = User.objects.filter(
        username__in=['gadhyac', 'faro', 'sakriye',
                      'cabdi_xasan', 'shine', 'sakariye_mxmed']
    )
    return render(request, 'menu/waiter_dashboard.html', {'waiters': waiters})

def waiter_tables(request, username):
    from django.contrib.auth.models import User
    waiter = User.objects.get(username=username)
    tables = Table.objects.filter(waiter=waiter)
    return render(request, 'menu/waiter_tables.html', {
        'tables': tables,
        'waiter': waiter
    })

def take_order(request, table_number):
    from django.contrib.auth.models import User
    table = Table.objects.get(number=table_number)
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()

    waiter_username = request.GET.get('waiter', '')
    waiter = None
    if waiter_username:
        try:
            waiter = User.objects.get(username=waiter_username)
        except:
            pass

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '')
        payment_method = request.POST.get('payment_method', 'cash')
        waiter_username = request.POST.get('waiter_username', '')

        try:
            waiter = User.objects.get(username=waiter_username)
        except:
            waiter = None

        new_order = Order.objects.create(
            customer_name=customer_name,
            item='Multiple Items',
            quantity=1,
            table=table,
            waiter=waiter,
            payment_method=payment_method,
            total_price=0
        )

        total = 0
        item_ids = request.POST.getlist('item_ids')
        quantities = request.POST.getlist('quantities')

        for item_id, qty in zip(item_ids, quantities):
            qty = int(qty)
            if qty > 0:
                menu_item = MenuItem.objects.get(id=item_id)
                subtotal = menu_item.price * qty
                total += subtotal
                OrderItem.objects.create(
                    order=new_order,
                    menu_item=menu_item,
                    quantity=qty,
                    price=menu_item.price
                )
                menu_item.daily_sold += qty
                if menu_item.daily_limit > 0 and menu_item.daily_sold >= menu_item.daily_limit:
                    menu_item.available = False
                menu_item.save()

        new_order.total_price = total
        new_order.save()
        table.is_busy = True
        table.save()

        return redirect('receipt', pk=new_order.pk)

    return render(request, 'menu/take_order.html', {
        'table': table,
        'categories': categories,
        'menu_items': menu_items,
        'waiter': waiter
    })

def mark_table_free(request, table_number):
    table = Table.objects.get(number=table_number)
    table.is_busy = False
    table.save()
    waiter_username = request.GET.get('waiter', '')
    return redirect(f'/waiter/{waiter_username}/')

def daily_report(request):
    from django.utils import timezone
    from django.db.models import Sum

    today = timezone.now().date()
    today_orders = Order.objects.filter(date__date=today)
    total_money = today_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
    cash_total = today_orders.filter(payment_method='cash').aggregate(Sum('total_price'))['total_price__sum'] or 0
    zaad_total = today_orders.filter(payment_method='zaad').aggregate(Sum('total_price'))['total_price__sum'] or 0
    edahab_total = today_orders.filter(payment_method='edahab').aggregate(Sum('total_price'))['total_price__sum'] or 0
    mastercard_total = today_orders.filter(payment_method='mastercard').aggregate(Sum('total_price'))['total_price__sum'] or 0

    return render(request, 'menu/daily_report.html', {
        'today_orders': today_orders,
        'total_money': total_money,
        'total_orders': today_orders.count(),
        'cash_total': cash_total,
        'zaad_total': zaad_total,
        'edahab_total': edahab_total,
        'mastercard_total': mastercard_total,
        'today': today,
    })

def mark_item_finished(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    item.available = False
    item.save()
    waiter_username = request.GET.get('waiter', '')
    return redirect(f'/take-order/{request.GET.get("table", 1)}/?waiter={waiter_username}')

def reset_menu(request):
    MenuItem.objects.all().update(available=True, daily_sold=0)
    return redirect('/')