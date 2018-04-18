from django import forms
from search.models import Book


class UserPanelBooksOwnedForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea,
    )

    class Meta:
        model = Book
        fields = ('author', 'title', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label = 'Autor'
        self.fields['title'].label = 'Tytuł'
        self.fields['description'].label = 'Opis'
        self.fields['description'].required = False


class UserPanelBooksWantedForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label = 'Autor'
        self.fields['title'].label = 'Tytuł'