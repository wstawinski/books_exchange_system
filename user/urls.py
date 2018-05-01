from django.urls import path
from .views import home, register, forgot_password, reset_password, exchanges
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
    path('home/<int:user_id>/', home, name='user_home'),
    path('login', LoginView.as_view(form_class=LoginForm, template_name='user/login.html'), name='user_login'),
    path('logout', LogoutView.as_view(), name='user_logout'),
    path('register', register, name='user_register'),
    path('forgot_password', forgot_password, name='user_forgot_password'),
    path('reset_password/<int:user_id>/<str:code>/', reset_password, name='user_reset_password'),
    path('reset_password', reset_password, name='user_reset_password'),
    path('exchanges', exchanges, name='user_exchanges')
]
