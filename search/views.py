from django.shortcuts import render

from search.forms import SearchForm
from search.models import Book, Tag


def search(request):
    if 'author' in request.GET and 'title' in request.GET and 'location' in request.GET:
        form = SearchForm(request.GET)
        books = None
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            location = form.cleaned_data['location']
            tags = request.GET.getlist('tags')

            books = Book.objects.filter(booktype_id=1, is_available=True)
            if author:
                books = books.filter(author__icontains=author)
            if title:
                books = books.filter(title__icontains=title)
            if location:
                books = books.filter(user__profile__location__icontains=location)

            books = books.filter(booktag__tagId__tag__in=tags)

    else:
        form = SearchForm()
        books = None

    tags = Tag.objects.all()

    return render(request, 'search/form.html', {'form': form, 'books': books, 'tags': tags})

