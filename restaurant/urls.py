from django.contrib import admin
from django.urls import path, include
from menu import views
from accounts import views as auth_views

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
]