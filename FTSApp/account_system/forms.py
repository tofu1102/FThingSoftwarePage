from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User


class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    error_messages = {
        'invalid_login': (
            "正しいユーザー名とパスワードを入力してください。"
            "注意: 両方のフィールドは大文字と小文字が区別されます。"
        ),
        'inactive': "このアカウントは無効です。",
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label   


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)
