from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import LoginForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm

class sign_in(LoginView):
    form_class = LoginForm
    template_name = 'account_system/sign_in.html'

class sign_out(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'account_system/sign_in.html'

@login_required
def account_setting(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_system:account_setting')  # 情報更新後にリダイレクト
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'account_system/account_settings.html', {'form': form})
    

def index(request):
    return render(request, "account_system/index.html")

def sign_up(request):
    return HttpResponse("sign up")

def password_reset(request):
    return HttpResponse("password_reset")

def test(request):
    return HttpResponse("test")

# Create your views here.
