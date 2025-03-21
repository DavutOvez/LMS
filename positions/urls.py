from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',position_table),
    path('delete/<int:pk>/',position_delete),
    path('edit/<int:pk>/',position_edit),
    path('create/',position_create)
]