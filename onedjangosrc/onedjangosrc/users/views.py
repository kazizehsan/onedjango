from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from .forms import AuthenticationForm


# Create your views here.
class LoginView(BaseLoginView):
    form_class = AuthenticationForm
