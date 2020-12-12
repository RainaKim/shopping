from django.shortcuts import redirect
from .models import User

def login_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/user/login')
        user = User.objects.get(email = user)
        request.user = user
        return func(request, *args, **kwargs)
    return wrap