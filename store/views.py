from django.shortcuts import render

# Create your views here.
def Products(request):
    return render(request, 'store/products.html')