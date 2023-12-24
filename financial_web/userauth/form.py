from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User


class RegistrationForm(UserCreationForm):
    """creating a registration form with django inbuilt form"""

    class Meta:
        """ overwriting the UsercreationForm fields"""

        model = User
        fields = ['username', 'email', 'password1', 'password2']