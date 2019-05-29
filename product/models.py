from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	price = models.FloatField()
	sale_start = models.DateTimeField('Start Date',null=True,blank=True)
	sale_end = models.DateTimeField('End Date',null=True,blank=True)
	is_on_sale = models.BooleanField(max_length=100)
	current_price = models.FloatField()


class ShopingCartItem(models.Model):
	product=models.CharField(max_length=100)
	quantity=models.FloatField()