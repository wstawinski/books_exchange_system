from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group


@login_required
def home(request):
    return render(request, 'user/home.html')


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
