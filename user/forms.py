from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.forms import UsernameField


class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Hasła nie są takie same.',
        'text_not_valid': 'Zawartość musi składać się wyłącznie z liter lub cyfr.',
        'password_to_short': 'Podaj dłuższe hasło.',
        'username_not_unique': 'Nazwa użytkownika jest już zajęta.',
        'email_not_unique': 'Użytkownik o podanym adresie email już istnieje.',
    }
    text_validator = RegexValidator(
        regex='^[\w]*$',
        message=error_messages['text_not_valid'],
    )
    password_validator = MinLengthValidator(
        8,
        message=error_messages['password_to_short'],
    )
    location = forms.CharField(
        max_length=50,
        label='Miasto',
        validators=[text_validator],
    )
    password1 = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput,
        validators=[password_validator],
        help_text='Hasło musi składać się przynajmniej z 8 znaków.',
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        widget=forms.PasswordInput,
        validators=[password_validator],
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'location', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Nazwa użytkowika'
        self.fields['username'].help_text = ''
        self.fields['username'].validators = [self.text_validator]

        self.fields['first_name'].label = 'Imię'
        self.fields['first_name'].required = True
        self.fields['first_name'].validators = [self.text_validator]

        self.fields['last_name'].label = 'Nazwisko'
        self.fields['last_name'].required = True
        self.fields['last_name'].validators = [self.text_validator]

        self.fields['email'].label = 'Adres email'
        self.fields['email'].required = True

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']):
            raise forms.ValidationError(
                self.error_messages['username_not_unique']
            )
        return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError(
                self.error_messages['email_not_unique']
            )
        return self.cleaned_data['email']


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Podaj poprawne dane logowania.',
        'inactive': 'Konto jest nieaktywne.',
    }
    username = UsernameField(
        label='Nazwa użytkownika',
        max_length=150,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput,
    )
