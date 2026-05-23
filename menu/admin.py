from django.contrib import admin
from .models import Order, MenuItem, Category, Table

admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Table)