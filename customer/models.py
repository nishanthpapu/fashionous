from django.db import models
from seller.models import *

# Create your models here.
class Customer(models.Model):
    email=models.EmailField(null=True)
    password=models.TextField(max_length=100,null=True)
    firstname=models.TextField(max_length=100,null=True)
    lastname=models.TextField(max_length=100,null=True)
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    

