from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    # '/music/'
    path('', views.index, name='index'),
    # '/music/3'
    re_path('(?P<album_id>[0-9]+)/', views.album_detail, name='detail'),
    # '/music/favourites'
    re_path('(?P<album_id>[0-9]+)/favourite', views.favourite, name='favourite'),
]
