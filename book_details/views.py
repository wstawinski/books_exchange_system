from django.http import Http404
from django.shortcuts import render, get_object_or_404
from search.models import Book, Images


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    images = Images.objects
    images = images.filter(bookId=book)
    for i in images:
        print(i.bookId)

    if book.is_available is False:
        raise Http404()
    return render(request, 'book_details/book.html', {'book': book, 'images': images})


def book_details_short(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details/book_short.html', {'book': book})
