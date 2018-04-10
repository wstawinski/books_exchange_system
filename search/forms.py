from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.forms import UsernameField

from search.models import Book


class SearchForm(forms.Form):
    error_messages = {
        'author_not_valid': 'Nazwa autora musi składać się wyłącznie z liter lub cyfr.',
        'title_not_valid': 'Tytuł musi składać się wyłącznie z liter lub cyfr.',
        'location_not_valid': 'Lokalizacja musi składać się wyłącznie z liter lub cyfr.',
    }
    author_validator = RegexValidator(
        regex='^[\w]*$',
        message=error_messages['author_not_valid'],
    )
    title_validator = RegexValidator(
        regex='^[\w]*$',
        message=error_messages['title_not_valid'],
    )
    location_validator = RegexValidator(
        regex='^[\w]*$',
        message=error_messages['location_not_valid'],
    )
    author = forms.CharField(
        max_length=150,
        label='Autor',
        validators=[author_validator],
    )
    title = forms.CharField(
        max_length=150,
        label='Tytuł',
        validators=[title_validator],
    )
    location = forms.CharField(
        max_length=50,
        label='Lokalizacja',
        validators=[location_validator],
    )

    class Meta:
        model = Book
        fields = ('author', 'title', 'location',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label = 'Autor'
        self.fields['author'].help_text = ''
        self.fields['author'].required = False
        self.fields['author'].validators = [self.author_validator]

        self.fields['title'].label = 'Tytuł'
        self.fields['title'].help_text = ''
        self.fields['title'].required = False
        self.fields['title'].validators = [self.title_validator]

        self.fields['location'].label = 'Lokalizacja'
        self.fields['location'].help_text = ''
        self.fields['location'].required = False
        self.fields['location'].validators = [self.location_validator]

    def clean(self):
        author = self.cleaned_data.get('author')
        title = self.cleaned_data.get('title')
        location = self.cleaned_data.get('location')

        if not author and not title and not location:
            raise forms.ValidationError("Ustawienie chociaż jednego z pól jest wymagane.")

        return self.cleaned_data

