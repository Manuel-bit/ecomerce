from django.shortcuts import render, redirect
from .forms import CreateUserForm
from store.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import auth


# Create your views here.
def Register(request):
    form = CreateUserForm()
    title = "customer Register"
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='Customers')
            user.groups.add(group)

            Customer.objects.create(
                user=user
            )

            return redirect('products')
    context = {
        'form':form,
        'title': title
    }
    return render(request, 'users/register.html', context)


def LogIn(request):
    if request.user.is_authenticated():
        return redirect('products')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('products')
    
    return render(request, 'users/login.html')