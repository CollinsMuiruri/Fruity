from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']
        # Add more fields as per your requirements

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price')
        # Add more fields as needed for product creation