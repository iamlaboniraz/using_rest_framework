"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import product.api_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products',product.api_views.ProductList.as_view()), 
    path('api/products/<int:id>/destroy',product.api_views.ProductDestroy.as_view()),
    path('api/products/<int:id>',product.api_views.ProductRetrieveUpdateDestroy.as_view()),
    path('api/products/new',product.api_views.PreductCreate.as_view()),
]
