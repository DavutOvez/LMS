from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',student_table),
    path('delete/<int:pk>/',student_delete),
    path('edit/<int:pk>/',student_edit),
    path('create/',student_create),
    path('profile/<int:pk>/',detail)
]