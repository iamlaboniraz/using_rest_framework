from rest_framework.exceptions import ValidationError # for Error msg
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView # for list,create,update,delete view
from product.serializers import ProductSerializer

# import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from product.models import Product


class ProductPagination(LimitOffsetPagination):
	default_limit=10
	max_limit=100

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields =('id',)
    search_fields = ('name','current_price')
    pagination_class=ProductPagination

    def get_queryset(self):
    	on_sale=self.request.query_params.get('on_sale',None)
    	if on_sale is None:
    		return super().get_queryset()
    	queryset=Product.objects.all()
    	if on_sale.lower() == 'true':
    		from django.utils import timezone
    		now=timezone.now()
    		return queryset.filter(
                  sale_start_lte=now,
                  sale_start_gte=now,
    			)
    	return queryset

## product create view ###
class PreductCreate(CreateAPIView):
	serializer_class = ProductSerializer
	def create(self,request,*args,**kwargs):
		try:
			price =request.data.get('price')
			if price is not None and float(price)<=0.0:
				raise ValidationError({'price':'Must be above $0.00'})
		except ValueError:
			raise ValidationError({'price':'A valid numbers required'})
		return super().create(request,*args,**kwargs)

### product destroy ##
class ProductDestroy(DestroyAPIView):
	queryset=Product.objects.all()
	lookup_field='id'
	def delete(self,request,*args,**kwargs):
		product_id=request.data.get('id')
		response=super().delete(request,*args,**kwargs)
		if response.status_code==204:
			from django.core.cache import cache
			cache.delete('product_data_{}'.format(product_id))
		return response

## product update and destroy ##

class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset=Product.objects.all()
	lookup_field='id'
	serializer_class=ProductSerializer

	def delete(self,request,*args,**kwargs):
		product_id=request.data.get('id')
		response=super().delete(request,*args,**kwargs)
		if response.status_code==204:
			from django.core.cache import cache
			cache.delete('product_data_{}'.format(product_id))
		return response

	def update(self,request,*args,**kwargs):
		response=super().update(request,*args,**kwargs)
		if response.status_code==200:
			from django.core.cache import cache
			product=response.data
			cache.set('product_data_{}'.format(product['id']),
                 {
                 'name':product['name'],
                 'description':product['description'],
                 'price':product['price'],
                 
                 })
			return response