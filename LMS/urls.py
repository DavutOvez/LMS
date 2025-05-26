from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from subjects.views import*
from main.views import *
from employees.views import *
from django.conf.urls import handler403

handler403 = custom_403

urlpatterns = [
    #Level  <-> #Level
    path('login/',login_page,name='user_login'),
    path('logout/',logout_page,name='user_logout'),
    #-------------------------------------------
    path('levels/table/',levels_table),
    path('levels/edit/<int:pk>/',level_edit),
    path('levels/create/',level_create),
    path('levels/delete/<int:pk>/',level_delete),
    path('get_levels/',get_levels, name = 'levels.get_level'),
    #-------------------------------------------
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('groups/',include('groups.urls')),
    path('seasons/',include('seasons.urls')),
    path('departments/',include('departments.urls')),
    path('positions/',include('positions.urls')),
    path('employees/',include('employees.urls')),
    path('branches/',include('branches.urls')),
    path('students/',include('students.urls')),
    path('subjects/',include('subjects.urls')),
    path('rooms/',include('rooms.urls')),
    path('groups/',include('groups.urls')),
    #-------------------------------------------
    path('roles/table/',roles_table),
    path('roles/edit/<int:pk>/',role_edit),
    path('roles/create/',role_create),
    #-------------------------------------------


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)