from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',groups_table),
    path('delete/<int:pk>/',group_delete),
    path('edit/<int:pk>/',group_edit),
    path('create/',group_create),
    path('add/student/',group_stu_create)
]