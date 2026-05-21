from django.contrib import admin
from django.urls import path
from menu import views
from accounts import views as auth_views
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username='sayid').exists():
        User.objects.create_superuser('sayid', 'sayid@email.com', 'sayid1234')
        return HttpResponse('Admin created!')
    return HttpResponse('Admin already exists!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', create_admin),
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
]