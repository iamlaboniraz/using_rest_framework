from django.contrib import admin

from .models import Product,ShopingCartItem

admin.site.register(Product)
admin.site.register(ShopingCartItem)
