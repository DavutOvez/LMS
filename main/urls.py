from django.urls import path , include
from .views import *


urlpatterns = [
    path('',index_page),
    path('login/',login_page)
]