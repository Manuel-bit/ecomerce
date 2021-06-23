from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.Register, name="customerRegister"),
    path('login/', views.LogIn, name="login"),
    path('logout/', views.logout, name="logout")
]