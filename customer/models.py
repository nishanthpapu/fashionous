from django.db import models

# Create your models here.
class Customer(models.Model):
    email=models.EmailField(null=True)
    password=models.TextField(max_length=100,null=True)
    firstname=models.TextField(max_length=100,null=True)
    lastname=models.TextField(max_length=100,null=True)
    

