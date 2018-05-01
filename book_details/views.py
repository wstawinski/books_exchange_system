from django.http import Http404
from django.shortcuts import render, get_object_or_404
from search.models import Book


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.is_available is False:
        raise Http404()
    return render(request, 'book_details/book.html', {'book': book})
