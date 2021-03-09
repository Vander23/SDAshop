from django import forms
from django.contrib.auth.models import User


class UserBasicDataChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(initial='Obecne hasło', min_length='8', widget=forms.PasswordInput, required=True)
    new_password1 = forms.CharField(initial='Nowe hasło', min_length='8', widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(initial='Powtórz hasło', min_length='8', widget=forms.PasswordInput, required=True)