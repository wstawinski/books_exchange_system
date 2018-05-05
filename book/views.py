from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from book.models import Exchange, ExchangeMessage
from search.models import Book
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime


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


@login_required
def exchange_details(request, exchange_id):
    exchange_obj = get_object_or_404(Exchange, pk=exchange_id)
    if not exchange_obj.initiator.id == request.user.id and not exchange_obj.receiver.id == request.user.id:
        raise Http404()
    initiator_books = Book.objects.filter(user_id=exchange_obj.initiator.id, booktype_id=1, is_available=True)
    exchange_messages = ExchangeMessage.objects.filter(exchange_id=exchange_obj.id)
    return render(request, 'book/exchange_details.html', {'exchange': exchange_obj, 'initiator_books': initiator_books,
                                                          'exchange_messages': exchange_messages})


@login_required
def exchange_choose_initiators_book(request):
    if request.method == 'POST':
        exchange_obj = get_object_or_404(Exchange, pk=request.POST['exchange_id'])
        initiators_book = get_object_or_404(Book, pk=request.POST['book_id'])
        if not exchange_obj.receiver.id == request.user.id:
            raise Http404()
        if not initiators_book.user.id == exchange_obj.initiator.id or initiators_book.booktype_id != 1 or initiators_book.is_available is False:
            raise Http404()
        exchange_obj.initiators_book_id = initiators_book.id
        exchange_obj.status_id = 3
        exchange_obj.save()
        return redirect('book_exchange_details', exchange_id=exchange_obj.id)


@login_required
def exchange_cancel(request):
    if request.method == 'POST':
        exchange_obj = get_object_or_404(Exchange, pk=request.POST['exchange_id'])
        if not exchange_obj.initiator.id == request.user.id and not exchange_obj.receiver.id == request.user.id:
            raise Http404()
        if exchange_obj.initiator.id == request.user.id:
            exchange_obj.status_id = 7
        else:
            exchange_obj.status_id = 8
        exchange_obj.date_closed = datetime.datetime.now()
        exchange_obj.save()
        return redirect('book_exchange_details', exchange_id=exchange_obj.id)


@login_required
def exchange_send_message(request):
    if request.method == 'POST':
        exchange_obj = get_object_or_404(Exchange, pk=request.POST['exchange_id'])
        if not exchange_obj.initiator.id == request.user.id and not exchange_obj.receiver.id == request.user.id:
            raise Http404()
        new_message = ExchangeMessage()
        new_message.message = request.POST['message_body']
        new_message.exchange_id = exchange_obj.id
        if exchange_obj.initiator.id == request.user.id:
            new_message.is_from_initiator = True
        else:
            new_message.is_from_initiator = False
        new_message.save()
        return redirect('book_exchange_details', exchange_id=exchange_obj.id)


@login_required
def exchange_successful(request):
    if request.method == 'POST':
        exchange_obj = get_object_or_404(Exchange, pk=request.POST['exchange_id'])
        if not exchange_obj.initiator.id == request.user.id and not exchange_obj.receiver.id == request.user.id:
            raise Http404()
        if exchange_obj.initiator.id == request.user.id:
            if exchange_obj.status.id == 5:
                exchange_obj.status_id = 6
                exchange_obj.date_closed = datetime.datetime.now()
                initiators_book = Book.objects.get(pk=exchange_obj.initiators_book.id)
                receivers_book = Book.objects.get(pk=exchange_obj.receivers_book.id)
                initiators_book.is_available = False
                receivers_book.is_available = False
                initiators_book.save()
                receivers_book.save()
            else:
                exchange_obj.status_id = 4
        else:
            if exchange_obj.status.id == 4:
                exchange_obj.status_id = 6
                exchange_obj.date_closed = datetime.datetime.now()
                initiators_book = Book.objects.get(pk=exchange_obj.initiators_book.id)
                receivers_book = Book.objects.get(pk=exchange_obj.receivers_book.id)
                initiators_book.is_available = False
                receivers_book.is_available = False
                initiators_book.save()
                receivers_book.save()
            else:
                exchange_obj.status_id = 5
        exchange_obj.save()
        return redirect('book_exchange_details', exchange_id=exchange_obj.id)
