import rest_framework

from rest_framework import serializers
from product.models import Product,ShopingCartItem

class CartItemSerialiser(serializers.ModelSerializer):
	class Meta:
		model=ShopingCartItem
		fields=(
             'product',
             'quantity'
			)


class ProductSerializer(serializers.ModelSerializer):
	is_on_sale = serializers.BooleanField(read_only=True)
	current_price=serializers.FloatField(read_only=True)
	description=serializers.CharField(min_length=1,max_length=100)
	# cart_item = serializers.SerializerMethodField()
	class Meta:
		model=Product
		fields=('id','name','description','price',
			'sale_start','sale_end','is_on_sale',
			'current_price')
	# def to_representation(self,instance):
	# 	data=super().to_representation(instance)
	# 	#data['is_on_sale']=instance.is_on_sale()
	# 	data['current_price']=instance.current_price()
	# 	return data

