from django.urls import path
from .views import create,home,login,logout

urlpatterns = [
    # path('/register', RegisterView.as_view()),
    path('/register', create),
    path('/login', login),
    path('/', home),
    path('/logout',logout)
]