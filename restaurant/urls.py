from django.contrib import admin
from django.urls import path
from menu import views
from accounts import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

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
    path('report/', views.daily_report, name='daily_report'),
    path('item-finished/<int:item_id>/', views.mark_item_finished, name='mark_item_finished'),
    path('reset-menu/', views.reset_menu, name='reset_menu'),
    path('debts/', views.debt_list, name='debt_list'),
    path('debts/add/', views.add_debt, name='add_debt'),
    path('debts/paid/<int:debt_id>/', views.mark_debt_paid, name='mark_debt_paid'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
