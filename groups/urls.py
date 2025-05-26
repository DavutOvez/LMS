from django.urls import path , include
from .views import *


urlpatterns = [
    path('table/',groups_table),
    path('delete/<int:pk>/',group_delete),
    path('edit/<int:pk>/',group_edit),
    path('create/',group_create),
    path('timetable/',group_timetable),
    path('add_teacher/',add_teacher),
    path('add_student/<int:pk>/',student),
    path('student/delete/<int:sp>/<int:gp>/',remove_student)
]