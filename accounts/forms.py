from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.transaction import atomic


class ProfileCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']
        # exclude = ['phone_number', 'nip_number', 'delivery_address', 'bank_account_number']

    nip_number = forms.IntegerField(label='NIP number')
    phone_number = forms.IntegerField(label='Phone number')
    delivery_address = forms.CharField(label='Delivery address')
    bank_account_number = forms.IntegerField(label='Bank account')

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        result = super().save(commit)
        nip_number = self.cleaned_data['nip_number']
        phone_number = self.cleaned_data['phone_number']
        delivery_address = self.cleaned_data['delivery_address']
        bank_account_number = self.cleaned_data['bank_account_number']
        profile = models.UserProfile(nip_number=nip_number, phone_number=phone_number,
                                     delivery_address=delivery_address, user=result,
                                     bank_account_number=bank_account_number)
        if commit:
            profile.save()
        return result


# class UserBasicDataChangeForm(forms.ModelForm):
#     class Meta:
#         model = models.UserProfile
#         fields = ['phone_number']


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(initial='Obecne hasło', min_length='8', widget=forms.PasswordInput, required=True)
    new_password1 = forms.CharField(initial='Nowe hasło', min_length='8', widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(initial='Powtórz hasło', min_length='8', widget=forms.PasswordInput, required=True)