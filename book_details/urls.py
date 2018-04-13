from django.urls import path
from book_details.views import book_details

urlpatterns = [
    path('<int:book_id>', book_details, name='book_details'),
]