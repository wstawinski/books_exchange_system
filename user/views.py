from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from search.models import Book
from .forms import RegisterForm, ForgotPasswordForm, ResetPasswordForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group, User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


@login_required
def home(request, user_id):
    user_profile = User.objects.get(pk=user_id)
    books_owned = Book.objects.filter(user_id=user_id).filter(booktype_id=1)
    books_wanted = Book.objects.filter(user_id=user_id).filter(booktype_id=2)
    return render(request, 'user/home.html', {'user_profile': user_profile, 'books_owned': books_owned, 'books_wanted': books_wanted})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.location = form.cleaned_data['location']
            user_group = Group.objects.get(name='user')
            user.groups.add(user_group)
            user.save()
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('user_home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email_address'])[0]
            password_reset_code = get_random_string(length=50)
            user.profile.password_reset_code = password_reset_code
            user.save()
            send_mail(
                'Przywracanie hasła',
                'Aby ustanowić nowe hasło, kliknij poniższy link:\n'
                'http://127.0.0.1:8000/user/reset_password/'+str(user.id)+'/'+str(password_reset_code)+'/',
                'SystemWymianyKsiążek',
                [request.POST['email_address']],
            )
            return render(request, 'user/reset_password_email_sent.html')
    else:
        form = ForgotPasswordForm()
    return render(request, 'user/forgot_password.html', {'form': form})


def reset_password(request, user_id=None, code=None):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        user_id = request.POST['user_id']
        code = request.POST['code']
        if form.is_valid():
            user = User.objects.get(pk=user_id)
            if user.profile.password_reset_code != code:
                raise Http404
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'user/reset_password_successful.html')
    else:
        user = User.objects.get(pk=user_id)
        if user.profile.password_reset_code != code:
            raise Http404()
        form = ResetPasswordForm()
    return render(request, 'user/reset_password.html', {'form': form, 'user_id': user_id, 'code': code})
