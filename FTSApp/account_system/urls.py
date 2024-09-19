from django.urls import path

from . import views

app_name = 'account_system'

urlpatterns = [
    path("sign_up", views.sign_up, name = "sign_up"), #アカウント作成
    path("sign_in", views.sign_in.as_view(), name = "sign_in"), #ログイン
    path("sign_out", views.sign_out.as_view(), name = "sign_out"), #ログアウト
    path("password_reset", views.password_reset, name = "password_reset"), #パスワードリセット画面
]