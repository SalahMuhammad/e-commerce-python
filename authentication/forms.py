from django.contrib.auth.forms import UserCreationForm

from .models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']
