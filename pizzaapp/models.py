from django.db import models

# Create your models here.
#here we dont create model for username and password because django admin profile provides that directly to us.
class PizzaModel(models.Model):
    name=models.CharField(max_length=10)
    price=models.CharField(max_length=10)
class CustomerModel(models.Model):
    userid=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=10)
class OrderModel(models.Model):
    user=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    orderitems=models.CharField(max_length=10)
    orderstatus=models.CharField(max_length=10, null=True)