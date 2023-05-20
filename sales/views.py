from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Payment
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    # Add logic to fetch summaries and analytics
    return render(request, 'sales/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'sales/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    # Add logic to fetch the number of products sold
    return render(request, 'sales/product_detail.html', {'product': product})

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'sales/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'sales/order_detail.html', {'order': order})

@login_required
def payment_list(request):
    payments = Payment.objects.all()
    # Add logic to calculate total amounts in the shop
    return render(request, 'sales/payment_list.html', {'payments': payments})

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'sales/create_order.html', {'form': form})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_order')
    else:
        form = ProductForm()
    return render(request, 'sales/create_product.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    # Implement logout logic here
    return redirect('login')  # Assuming you have a login page URL named 'login'
