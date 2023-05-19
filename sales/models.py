from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as per your requirements

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # Add more fields as per your requirements

    def save(self, *args, **kwargs):
        if not self.order_id:
            last_order = Order.objects.order_by('-order_id').first()
            if last_order:
                last_order_id = last_order.order_id
                self.order_id = last_order_id + 1
            else:
                self.order_id = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Payment(models.Model):
    METHOD_CHOICES = [
        ('MPESA', 'M-PESA'),
        ('Cash', 'Cash'),
    ]
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as per your requirements
    
