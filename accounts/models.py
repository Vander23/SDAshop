from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=150, blank=True)
    email = models.EmailField(_('Email address'), blank=True)
    nip_number = models.IntegerField(_('NIP number'), blank=True, default=0)
    phone_number = models.IntegerField(_('Phone number'), blank=True, default=0)
    delivery_address = models.CharField(_('Delivery address'), max_length=100, blank=True, default="0")
    bank_account_number = models.IntegerField(_('Bank account'), blank=True, default=0)

    def __str__(self):
        return self.user.username
