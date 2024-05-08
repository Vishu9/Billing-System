# billing/admin.py
from django.contrib import admin
from .models import Product, Bill

admin.site.register(Product)
admin.site.register(Bill)
