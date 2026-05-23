from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Table(models.Model):
    number = models.IntegerField(unique=True)
    is_busy = models.BooleanField(default=False)
    waiter = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        status = "Busy" if self.is_busy else "Free"
        return f"Table {self.number} — {status}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    image = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('zaad', 'Zaad'),
        ('edahab', 'eDahab'),
        ('mastercard', 'Mastercard'),
    ]
    
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    waiter = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cash')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer_name} — Table {self.table}"