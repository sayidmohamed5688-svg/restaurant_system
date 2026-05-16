from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} — {self.item}"