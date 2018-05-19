from django import forms
from search.models import Book
from search.models import Images


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


#nieużywane, bo trzeba w <input> jebnąć MULTIPLE a stąd się nie da.
class UserPanelBooksOwnedFormImage(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].label = 'Zdjęcie'
        self.fields['image'].required = False


class UserPanelBooksWantedForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].label = 'Autor'
        self.fields['title'].label = 'Tytuł'