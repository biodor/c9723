from django import forms
from django.contrib.auth.models import User
from council.models import OfficersTerm
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class OfficersTermForm(forms.ModelForm):

    class Meta:
        model = OfficersTerm
        fields = ['colbn_year', 'council_number', 'membership_number', 'name', 'position', 'installed_date']

