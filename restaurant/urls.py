from django.contrib import admin
from django.urls import path
from menu import views
from accounts import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_waiters(request):
    waiters = ['gadhyac', 'faro', 'sakriye', 'cabdi_xasan', 'shine', 'sakariye_mxmed']
    for w in waiters:
        if not User.objects.filter(username=w).exists():
            User.objects.create_user(username=w, password='waiter1234')
    return HttpResponse('Waiters created!')

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
    path('create-waiters/', create_waiters),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
