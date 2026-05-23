from django.contrib import admin
from .models import Order, MenuItem, Category

admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Category)