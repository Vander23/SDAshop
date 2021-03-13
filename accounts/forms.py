from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(UserCreationForm):
    phone_number = forms.IntegerField()


class UserBasicDataChangeForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['first_name', 'last_name', 'phone_number']


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(initial='Obecne hasło', min_length='8', widget=forms.PasswordInput, required=True)
    new_password1 = forms.CharField(initial='Nowe hasło', min_length='8', widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(initial='Powtórz hasło', min_length='8', widget=forms.PasswordInput, required=True)