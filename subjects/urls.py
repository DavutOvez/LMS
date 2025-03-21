from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',subjects_table),
    path('delete/<int:pk>/',subject_delete),
    path('edit/<int:pk>/',subject_edit),
    path('create/',subject_create)
]