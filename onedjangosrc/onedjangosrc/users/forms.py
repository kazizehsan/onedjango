from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, \
    UserChangeForm as BaseUserChangeForm, AuthenticationForm as BaseAuthenticationForm, UsernameField

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        # Doesn't affect Admin Panel, since there `UserAdmin`.`add_fieldsets` takes precedence over `fields`.
        fields = ('email', 'date_of_birth')


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = '__all__'


class AuthenticationForm(BaseAuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True, 'class': 'form-control mt-1', 'placeholder': "Email Address"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password', 'class': 'form-control mt-1', 'placeholder': "Password"}),
    )
