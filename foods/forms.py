from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from .models import User
from .validators import PhoneValidator

class UserRegistrationForm(UserCreationForm):

    phone = forms.CharField(max_length=14, )
    # password = forms.CharField(max_length=100,
    #             widget=forms.PasswordInput, required=True,
    #             validators=[MinLengthValidator(8)])
    # confirm = forms.CharField(max_length=100,
    #             widget=forms.PasswordInput, required=True,
    #             validators=[MinLengthValidator(8)])


    class Meta:
        model=User
        fields = ['username', 'first_name', "last_name", 'phone', 'password1', 'password2']
