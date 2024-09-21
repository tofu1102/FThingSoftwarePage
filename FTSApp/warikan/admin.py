from django.contrib import admin


from .models import Event, Payment


admin.site.register([Event, Payment])  # Userモデルを登録
# Register your models here.
