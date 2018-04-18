from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.forms import UsernameField

from search.models import Book


class SearchForm(forms.Form):
    author = forms.CharField(
        max_length=150,
        label='Autor',
        required=False,
    )
    title = forms.CharField(
        max_length=150,
        label='Tytuł',
        required=False,
    )
    location = forms.CharField(
        max_length=50,
        label='Lokalizacja',
        required=False,
    )

    def clean(self):
        author = self.cleaned_data.get('author')
        title = self.cleaned_data.get('title')
        location = self.cleaned_data.get('location')

        if not author and not title and not location:
            raise forms.ValidationError("Ustawienie chociaż jednego z pól jest wymagane.")

        return self.cleaned_data

