from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.forms import UsernameField

from search.models import Book


class SearchForm(forms.Form):
    error_messages = {
        'title_not_valid': 'Tytuł ksiażek musi składać się wyłącznie z liter lub cyfr.',
    }
    title_validator = RegexValidator(
        regex='^[\w]*$',
        message=error_messages['title_not_valid'],
    )
    title = forms.CharField(
        max_length=50,
        label='Tytuł',
        validators=[title_validator],
    )

    class Meta:
        model = Book
        # fields = ('username', 'first_name', 'last_name', 'location', 'email', 'password1', 'password2',)
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = 'Tytuł książki'
        self.fields['title'].help_text = ''
        self.fields['title'].required = True
        self.fields['title'].validators = [self.title_validator]

        # self.fields['first_name'].label = 'Imię'
        # self.fields['first_name'].required = True
        # self.fields['first_name'].validators = [self.text_validator]

        # self.fields['last_name'].label = 'Nazwisko'
        # self.fields['last_name'].required = True
        # self.fields['last_name'].validators = [self.text_validator]

        # self.fields['email'].label = 'Adres email'
        # self.fields['email'].required = True

