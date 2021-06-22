from django.shortcuts import render
from .models import Product


# Create your views here.
def Products(request):
    products = Product.objects.all()
    title = "Our Products"
    context = {
        "products":products,
        "title":title
    }
    return render(request, 'store/products.html', context)

def Cart(request):
    return render(request, 'store/cart.html')