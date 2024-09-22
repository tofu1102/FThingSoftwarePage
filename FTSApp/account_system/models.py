import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage

class User(AbstractUser):
    # UUIDをプライマリキーとして使用する
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    # LINEのユーザーIDを保存するフィールド
    line_user_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    # LINEの表示名を保存するフィールド
    line_display_name = models.CharField(max_length=255, null=True, blank=True)
    # LINEのプロフィール画像URLを保存するフィールド
    line_picture_url = models.URLField(max_length=1024, null=True, blank=True)
    # LINE登録されているか?
    line_authorized = models.BooleanField(default=False)
    
    # メールアドレスをユーザー名として使用
    email = models.EmailField(unique=True)  # ユニーク制約を追加

    # 必須フィールドの設定
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def icon_url(self):
        """ユーザーのアイコン画像URLを返す
        1. SNS認証時にプロフィール画像を取得できた場合: sns_icon_url
        2. SNS認証時にプロフィール画像を取得できなかった場合: デフォルト画像
        """
        if self.line_picture_url:
            return self.line_picture_url
        return staticfiles_storage.url("images/FTS.png")


    def __str__(self):
        return self.username
