from django.shortcuts import render, render_to_response
from search.models import Book


def book_details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return render_to_response('book_details/noSuchBook.html', {'book_id': book_id})

    return render(request, 'book_details/book.html', {'book': book})