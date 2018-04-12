from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user_panel.forms import UserPanelBooksOwnedForm, UserPanelBooksWantedForm
from search.models import Book


@login_required
def user_panel_booksOwned(request):
    form = UserPanelBooksOwnedForm(request.POST)
    books = Book.objects
    books = books.filter(user_id__exact=request.user).filter(booktype_id__exact=1)

    if request.method == 'POST':
        form = UserPanelBooksOwnedForm(request.POST)

        author = request.POST['author']
        title = request.POST['title']
        description = request.POST['description']

        if not author or not title:
            books = None
        else:
            book = Book()
            book.author = author
            book.title = title
            book.booktype_id = 1
            book.user_id = request.user.id
            books.description = description
            book.save()
    else:
        form = UserPanelBooksOwnedForm()

    return render(request, 'user_panel/user_panel_booksOwned.html', {'form': form, 'books': books})


@login_required
def user_panel_booksWanted(request):
    form = UserPanelBooksWantedForm(request.POST)
    books = Book.objects
    books = books.filter(user_id__exact=request.user).filter(booktype_id__exact=2)

    if request.method == 'POST':
        form = UserPanelBooksWantedForm(request.POST)

        author = request.POST['author']
        title = request.POST['title']

        if not author or not title:
            books = None
        else:
            book = Book()
            book.author = author
            book.title = title
            book.booktype_id = 2
            book.user_id = request.user.id
            book.save()
    else:
        form = UserPanelBooksWantedForm()

    return render(request, 'user_panel/user_panel_booksWanted.html', {'form': form, 'books': books})
