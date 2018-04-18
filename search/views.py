from django.shortcuts import render

from search.forms import SearchForm
from search.models import Book


def search(request):
    if 'author' in request.GET and 'title' in request.GET and 'location' in request.GET:
        form = SearchForm(request.GET)
        books = None
        if form.is_valid():
            author = request.GET['author']
            title = request.GET['title']
            location = request.GET['location']

            books = Book.objects.filter(booktype_id=1)
            if author:
                books = books.filter(author__icontains=author)
            if title:
                books = books.filter(title__icontains=title)
            if location:
                books = books.filter(user__profile__location__icontains=location)
    else:
        form = SearchForm()
        books = None

    return render(request, 'search/form.html', {'form': form, 'books': books})

