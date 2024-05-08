# billing/views.py
from django.shortcuts import render
from .models import Product, Bill

def generate_bill(request):
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        total_cost = sum(Product.objects.filter(id__in=selected_products).values_list('price', flat=True))
        bill = Bill.objects.create(total_cost=total_cost)
        bill.products.set(selected_products)
        bill.save()
        return render(request, 'billing/bill.html', {'bill': bill})
    else:
        products = Product.objects.all()
        return render(request, 'billing/generate_bill.html', {'products': products})
