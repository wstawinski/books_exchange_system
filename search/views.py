from django.shortcuts import render

from search.forms import SearchForm
from search.models import Book


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        title = request.POST['title']
        books = Book.objects.filter(title__icontains=title)
    else:
        form = SearchForm()
        books = None
    return render(request, 'search/form.html', {'form': form, 'books': books})

