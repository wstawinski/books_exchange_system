from django.urls import path
from .views import home, register
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
    path('home', home, name='user_home'),
    path('login', LoginView.as_view(form_class=LoginForm, template_name='user/login.html'), name='user_login'),
    path('logout', LogoutView.as_view(), name='user_logout'),
    path('register', register, name='user_register'),
]
