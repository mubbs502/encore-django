from django.urls import path

from . import api

urlpatterns = [
    path('', api.playlist_list, name='playlist_list'),
    path('retrieve/<name>', api.playlist_item, name='playlist_item'),
    path('create/', api.playlist_create, name='playlist_create')
]