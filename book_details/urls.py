from django.urls import path
from book_details.views import book_details, book_details_short

urlpatterns = [
    path('short/<int:book_id>/', book_details_short, name='book_details_short'),
    path('<int:book_id>', book_details, name='book_details'),
]