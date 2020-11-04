from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['full_name', 'email',
                  'phone_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['full_name', 'email', 'phone_number', 'image']
