from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user_panel.forms import UserPanelBooksOwnedForm, UserPanelBooksWantedForm, UserPanelBooksOwnedFormImage
from search.models import Book, Images, Tag, BookTag
from django.core.files.storage import FileSystemStorage


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

        #By bookid przypisać do zdjęcia
        books = Book.objects
        bookid = books.filter(user_id__exact=request.user, booktype_id__exact=1, is_available=True, author=author, title=title).order_by('-id')[0]
        for oneimage in request.FILES.getlist('image'):
            image = Images()
            image.bookId = bookid
            image.image = oneimage.name
            image.save()

            fs = FileSystemStorage()
            filename = fs.save(oneimage.name, oneimage)

        for tagStr in request.POST.getlist('tags'):
            print(tagStr)
            bk = BookTag()
            bk.bookId = bookid

            num_results = Tag.objects.filter(tag=tagStr).count()
            if num_results == 0:
                t = Tag()
                t.tag = tagStr
                t.save()

            bk.tagId = Tag.objects.get(tag=tagStr)
            bk.save()


    form = UserPanelBooksOwnedForm()
    books = Book.objects
    books = books.filter(user_id__exact=request.user, booktype_id__exact=1, is_available=True)

    #formImage = UserPanelBooksOwnedFormImage()

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
    books = books.filter(user_id__exact=request.user, booktype_id__exact=2, is_available=True)

    return render(request, 'user_panel/user_panel_booksWanted.html', {'form': form, 'books': books})


@login_required
def user_panel_removeBook(request):
    if request.method == 'POST':
        book_id = int(request.POST.get('book_id'))
        type_id = int(request.POST.get('type_id'))

        book = Book.objects.get(pk=book_id)
        book.is_available = False
        book.save()

        if type_id == 1:
            return redirect(user_panel_booksOwned)
        elif type_id == 2:
            return redirect(user_panel_booksWanted)