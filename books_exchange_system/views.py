from django.shortcuts import render


def index(request):
    return render(request, 'books_exchange_system/index.html')
