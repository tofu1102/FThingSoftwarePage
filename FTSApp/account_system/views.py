from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm 

class sign_in(LoginView):
    form_class = LoginForm
    template_name = 'sign_in.html'

class sign_out(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'sign_in.html'

def index(request):
    return render(request, "index.html")

def sign_up(request):
    return HttpResponse("sign up")

def password_reset(request):
    return HttpResponse("password_reset")

# Create your views here.
