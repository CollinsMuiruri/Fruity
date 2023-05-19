from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('payments/', views.payment_list, name='payment_list'),
    path('orders/create/', views.create_order, name='create_order'),
    path('products/create/', views.create_product, name='create_product'),
    path('logout/', views.logout, name='logout'),
]
