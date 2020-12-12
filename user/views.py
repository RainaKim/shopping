from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from .models import User
from product.models import Product
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'user':request.session.get('user'),'object_list':products})

def create(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                name = form.data.get('name'),
                email = form.data.get('email'),
                password = form.data.get('password'),
            )
            user.save()
            return HttpResponseRedirect('/')
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            if email and password :
                try:
                    user = User.objects.get(email = email)
                except User.DoesNotExist:
                    messages.info(request, 'Email does not exist')
                    return HttpResponseRedirect('/user/login')
            
                if password != user.password:
                    messages.info(request, 'Incorrect password')
                request.session['user'] = form.data.get('email')
                return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

def logout(request):
    if request.session.get('user'):
        if request.session.get('user'):
            del(request.session['user'])
        return HttpResponseRedirect('/')
