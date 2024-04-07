from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni tasdiqlash'}))

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.fields["email"].help_text = None
        self.fields["username"].help_text = None

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'}),
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}),
            # 'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parol 1'}),
            # "password2": forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parol 2'}),
        }

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(
#         max_length=254,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
#     )
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#     )