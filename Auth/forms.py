from django import forms
from .models import *
from django.conf import settings
import re


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'is_active', 'avatar')
