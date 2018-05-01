from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from book.models import Exchange
from search.models import Book
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def exchange(request):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=request.POST['book_id'])
        if book.user.id == request.user.id or book.is_available is False:
            raise Http404()
        existing_exchange = Exchange.objects.filter(initiator_id=request.user.id, receivers_book_id=book.id) \
            .filter(~Q(status_id=2), ~Q(status_id=7), ~Q(status_id=8))
        if existing_exchange.count() != 0:
            messages.add_message(request, messages.ERROR, 'Proces wymiany wybranej książki został już zainicjowany.')
            return redirect('user_exchanges')
        new_exchange = Exchange()
        new_exchange.initiator_id = request.user.id
        new_exchange.receiver_id = book.user.id
        new_exchange.receivers_book_id = book.id
        new_exchange.status_id = 1
        new_exchange.save()
        messages.add_message(request, messages.SUCCESS, 'Pomyślnie zainicjowano nowy proces wymiany książki.')
        return redirect('user_exchanges')
