from django.urls import path

from . import views

app_name = 'warikan'

urlpatterns = [
    path("index/", views.index, name = "index"), #warikanのindex
    path("event_detail/<uuid:uuid>/", views.event_detail, name = "event_detail"), #イベント詳細ページ
    path('event/<uuid:event_uuid>/payments/<uuid:payment_uuid>/', views.payment_detail, name='payment_detail'),
    path('event/<uuid:event_uuid>/payments/', views.payment_list, name='payment_list'),
    path('event_detail/<uuid:uuid>/confirmation/', views.confirmation, name="confirmation"),
    path('add_event/', views.add_event, name="add_event"),
    path('event/invite/<uuid:event_uuid>/', views.invite, name="invite"),
]