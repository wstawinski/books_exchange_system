from django.urls import path
from .views import search
from django.contrib.auth.views import LoginView, LogoutView
#from .forms import LoginForm

urlpatterns = [
    path('search', search, name='search'),
]