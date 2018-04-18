from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user_panel.forms import UserPanelBooksOwnedForm, UserPanelBooksWantedForm
from search.models import Book


@login_required
def user_panel_booksOwned(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        description = request.POST['description']

        book = Book()
        book.author = author
        book.title = title
        book.description = description
        book.booktype_id = 1
        book.user_id = request.user.id
        book.save()

    form = UserPanelBooksOwnedForm()
    books = Book.objects
    books = books.filter(user_id__exact=request.user).filter(booktype_id__exact=1)

    return render(request, 'user_panel/user_panel_booksOwned.html', {'form': form, 'books': books})


@login_required
def user_panel_booksWanted(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']

        book = Book()
        book.author = author
        book.title = title
        book.booktype_id = 2
        book.user_id = request.user.id
        book.save()

    form = UserPanelBooksWantedForm()
    books = Book.objects
    books = books.filter(user_id__exact=request.user).filter(booktype_id__exact=2)

    return render(request, 'user_panel/user_panel_booksWanted.html', {'form': form, 'books': books})


@login_required
def user_panel_removeBook(request):
    if request.method == 'POST':
        book_id = int(request.POST.get('book_id'))
        type_id = int(request.POST.get('type_id'))
        Book.objects.filter(id=book_id).delete()

        if type_id == 1:
            return redirect(user_panel_booksOwned)
        elif type_id == 2:
            return redirect(user_panel_booksWanted)