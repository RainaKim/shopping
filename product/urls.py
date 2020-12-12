from django.urls import path
from .views import product_register

urlpatterns = [
    path('/register',product_register)
]