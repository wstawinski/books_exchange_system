from django.shortcuts import render

from search.forms import SearchForm
from search.models import Book


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        author = request.POST['author']
        title = request.POST['title']
        location = request.POST['location']

        if not author and not title and not location:
            books = None
        else:
            books = Book.objects
            if author:
                books = books.filter(author__icontains=author)
            if title:
                books = books.filter(title__icontains=title)
            if location:
                books = books.filter(location__icontains=location)
    else:
        form = SearchForm()
        books = None
    return render(request, 'search/form.html', {'form': form, 'books': books})

