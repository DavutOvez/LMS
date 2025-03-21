from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('table/',branch_table,name='branch_table'),
    path('delete/<int:pk>/',branch_delete),
    path('edit/<int:pk>/',branch_edit),
    path('create/',branch_create),
]