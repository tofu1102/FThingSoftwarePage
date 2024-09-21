from django.urls import path

from . import views

app_name = 'warikan'

urlpatterns = [
    path("index", views.index, name = "index"), #warikanのindex
    path("event_detail/<uuid:uuid>", views.event_detail, name = "event_detail"), #イベント詳細ページ
    path('events/<uuid:event_uuid>/payments/<uuid:payment_uuid>/', views.payment_detail, name='payment_detail'),
    path('event/<uuid:event_uuid>/payments/', views.payment_list, name='payment_list'),
]