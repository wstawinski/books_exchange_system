from django.shortcuts import render
from search.models import Book


def index(request):
    latest_books = Book.objects.filter(booktype_id=1, is_available=True).order_by('-pk')[:10]
    return render(request, 'books_exchange_system/index.html', {'latest_books':latest_books})
