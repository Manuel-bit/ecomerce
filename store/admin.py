from django.contrib import admin
from .models import Customer,Order,ShippingAddress,Product

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Customer)

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Order)

class ShippingAddressAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(ShippingAddress)