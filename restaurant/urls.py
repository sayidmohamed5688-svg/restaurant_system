from django.contrib import admin
from django.urls import path
from menu import views
from accounts import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.http import HttpResponse
from menu.models import Table

def create_tables(request):
    Table.objects.all().delete()
    for i in range(1, 101):
        Table.objects.create(number=i)
    return HttpResponse(f'Created {Table.objects.count()} tables!')

def assign_tables(request):
    gadhyac = User.objects.get(username='gadhyac')
    faro = User.objects.get(username='faro')
    sakriye = User.objects.get(username='sakriye')
    cabdi = User.objects.get(username='cabdi_xasan')
    shine = User.objects.get(username='shine')
    sakariye = User.objects.get(username='sakariye_mxmed')

    waiter_map = {1: gadhyac, 2: faro, 3: sakriye, 4: cabdi, 5: shine, 6: sakariye}

    for table in Table.objects.all():
        remainder = table.number % 10
        if remainder == 0:
            remainder = 10
        if remainder <= 6:
            table.waiter = waiter_map[remainder]
            table.save()

    return HttpResponse(f'Tables assigned! Total: {Table.objects.exclude(waiter=None).count()}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('orders/', views.all_orders, name='all_orders'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
    path('delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('search/', views.search, name='search'),
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register, name='register'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('dashboard/', views.waiter_dashboard, name='waiter_dashboard'),
    path('take-order/<int:table_number>/', views.take_order, name='take_order'),
    path('waiter/<str:username>/', views.waiter_tables, name='waiter_tables'),
    path('table-free/<int:table_number>/', views.mark_table_free, name='mark_table_free'),
    path('create-tables/', create_tables),
    path('assign-tables/', assign_tables),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
