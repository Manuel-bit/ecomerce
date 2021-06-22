from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Products, name="products"),
    path('cart/', views.Cart, name="shoppingcart")
]