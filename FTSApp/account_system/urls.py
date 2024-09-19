from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #全体の基本ページ
    path("log_on", views.log_on, name = "log_on"), #アカウント作成
    
]