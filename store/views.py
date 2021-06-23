from django.shortcuts import render
from .models import Product
from .models import Order


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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
    context = {
        'items':items,
        'order':order
    }

    return render(request, 'store/cart.html', context)

def CheckOut(request):
    return render(request, 'store/checkout.html')