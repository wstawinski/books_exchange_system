from django.urls import path
from user_panel.views import user_panel_booksOwned, user_panel_booksWanted

urlpatterns = [
    path('booksOwned', user_panel_booksOwned, name='user_panel_booksOwned'),
    path('booksWanted', user_panel_booksWanted, name='user_panel_booksWanted'),
]