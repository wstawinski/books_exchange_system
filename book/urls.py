from django.urls import path
from .views import exchange, exchange_details, exchange_choose_initiators_book, exchange_cancel, exchange_send_message, exchange_successful


urlpatterns = [
    path('exchange_successful', exchange_successful, name='book_exchange_successful'),
    path('exchange_send_message', exchange_send_message, name='book_exchange_send_message'),
    path('exchange_cancel', exchange_cancel, name='book_exchange_cancel'),
    path('exchange_choose_initiators_book', exchange_choose_initiators_book, name='book_exchange_choose_initiators_book'),
    path('exchange_details/<int:exchange_id>/', exchange_details, name='book_exchange_details'),
    path('exchange', exchange, name='book_exchange')
]