from django import forms
from django.core.validators import RegexValidator


from search.models import Book


class UserPanelBooksOwnedForm(forms.Form):
    error_messages = {
        'author_not_valid': 'Nazwa autora musi składać się wyłącznie z liter lub cyfr.',
        'title_not_valid': 'Tytuł musi składać się wyłącznie z liter lub cyfr.',
        'description_not_valid': 'Opis zawiera maksymalnie 1000 znaków'
    }
    author_validator = RegexValidator(
        #jakiego regexa  tu jebnąć BY SPACJE
        message=error_messages['author_not_valid'],
    )
    title_validator = RegexValidator(
        #
        message=error_messages['title_not_valid'],
    )
    description_validator = RegexValidator(
        #
        message=error_messages['description_not_valid'],
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
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=1000,
        label='Opis',
        validators=[description_validator],
    )

    class Meta:
        model = Book
        fields = ('author', 'title', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label = 'Autor'
        self.fields['author'].help_text = ''
        self.fields['author'].required = True
        self.fields['author'].validators = [self.author_validator]

        self.fields['title'].label = 'Tytuł'
        self.fields['title'].help_text = ''
        self.fields['title'].required = True
        self.fields['title'].validators = [self.title_validator]

        self.fields['description'].label = 'Opis'
        self.fields['description'].help_text = ''
        self.fields['description'].required = False
        self.fields['description'].validators = [self.description_validator]

    def clean(self):
        author = self.cleaned_data.get('author')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')

        return self.cleaned_data


class UserPanelBooksWantedForm(forms.Form):
    error_messages = {
        'author_not_valid': 'Nazwa autora musi składać się wyłącznie z liter lub cyfr.',
        'title_not_valid': 'Tytuł musi składać się wyłącznie z liter lub cyfr.',
    }
    author_validator = RegexValidator(
        message=error_messages['author_not_valid'],
    )
    title_validator = RegexValidator(
        message=error_messages['title_not_valid'],
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

    class Meta:
        model = Book
        fields = ('author', 'title')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label = 'Autor'
        self.fields['author'].help_text = ''
        self.fields['author'].required = True
        self.fields['author'].validators = [self.author_validator]

        self.fields['title'].label = 'Tytuł'
        self.fields['title'].help_text = ''
        self.fields['title'].required = True
        self.fields['title'].validators = [self.title_validator]

    def clean(self):
        author = self.cleaned_data.get('author')
        title = self.cleaned_data.get('title')

        return self.cleaned_data

