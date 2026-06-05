from django.contrib import admin
from .models import Order, MenuItem, Category, Table, OrderItem, CustomerDebt, InventoryItem

admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(OrderItem)
admin.site.register(CustomerDebt)
admin.site.register(InventoryItem)