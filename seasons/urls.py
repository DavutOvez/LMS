from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',seasons_table),
    path('delete/<int:pk>/',season_delete),
    path('edit/<int:pk>/',season_edit),
    path('create/',season_create)
]