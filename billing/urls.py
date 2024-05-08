# billing_system/urls.py
from django.urls import path
from billing.views import generate_bill


urlpatterns = [
    path('generate-bill/', generate_bill, name='generate_bill'),
    # Add other URL patterns as needed
]
