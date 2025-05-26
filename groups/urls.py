from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',groups_table),
    path('delete/<int:pk>/',group_delete),
    path('edit/<int:pk>/',group_edit),
    path('create/',group_create),
    path('timetable/',group_timetable),
]