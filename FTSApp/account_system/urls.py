from django.urls import path

from . import views

app_name = 'account_system'

urlpatterns = [
    path("sign_out", views.sign_out.as_view(), name = "sign_out"), #ログアウト
    path("account_setting", views.account_setting, name="account_setting"), #アカウント設定
]