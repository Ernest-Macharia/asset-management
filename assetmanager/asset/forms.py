
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from . models import Asset, Appreciate, Depreciate


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
            'password2': None,
            'password1': None
        }

    def clean_email(self):

        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com') and not email.endswith('@yahoo.com') and not email.endswith('@outlook.com'):

            raise ValidationError('Domain of email is not valid')

        return email

    def clean_first_name(self):

        first = self.cleaned_data['first_name']

        print(first.isalpha())

        if not first.isalpha():
            raise ValidationError('Name cannot be numeric')

        return first

    def clean_second_name(self):

        first = self.cleaned_data['last_name']

        print(first.isalpha())

        if not first.isalpha():
            raise ValidationError('Name cannot be numeric')

        return first


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name','serial_number','acquisition_date','departments','category']
    

class AppreciationForm(forms.ModelForm):
    class Meta:
        model = Appreciate
        exclude = []

class DepreciationForm(forms.ModelForm):
    class Meta:
        model = Depreciate
        exclude = []