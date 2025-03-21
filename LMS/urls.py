from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from subjects.views import*


urlpatterns = [
    #Level  <-> #Level
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


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)