from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',employee_table,name='employee_table'),
    path('delete/<int:pk>/',employee_delete),
    path('edit/<int:pk>/',employee_edit),
    path('create/',employee_create),
    path('profile/<int:pk>/',detail),
    path('create_user/<int:pk>/',create_user, name='employees.create_user'),
]