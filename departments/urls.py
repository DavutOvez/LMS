from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',departments_table),
    path('delete/<int:pk>/',department_delete),
    path('edit/<int:pk>/',department_edit),
    path('create/',department_create)
]