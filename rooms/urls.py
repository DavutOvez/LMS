from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',room_table,name='room_table'),
    path('delete/<int:pk>/',room_delete),
    path('edit/<int:pk>/',room_edit),
    path('create/',room_create),
    path('get_room/',get_room, name = 'rooms.get_room'),
]