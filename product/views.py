from django.shortcuts import render
from .models import Product
from user.models import User
from .forms import RegisterForm
from django.views.generic.edit import FormView
from user.utils import login_required
from django.http import HttpResponseRedirect

@login_required
def product_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            product = Product(
                name = form.data.get('name'),
                price = form.data.get('price'),
                owner = User.objects.get(id = request.user.id)
            )
            product.save()
            return HttpResponseRedirect('/')
    form = RegisterForm()
    return render(request, 'product_register.html', {'form':form})
