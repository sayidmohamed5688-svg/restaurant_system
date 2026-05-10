from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('orders/', views.all_orders, name='all_orders'),
    path('receipt/<int:pk>/', views.receipt, name='receipt'),
]