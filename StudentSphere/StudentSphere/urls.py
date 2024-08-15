from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, HOD_Views, Staff_Views, Students_Views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),

                  path('', views.LOGIN, name='login'),
                  path('doLogin/', views.doLogin, name='doLogin'),
                  path('doLogout/', views.doLogout, name='logout'),

                  path('profile/', views.PROFILE, name='profile'),
                  path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  path('HOD/home', HOD_Views.home, name='HOD_home'),
                  path('HOD/Student/ADD', HOD_Views.ADD_STUDENTS, name='add_students'),
                  path('HOD/Student/View', HOD_Views.VIEW_STUDENTS, name='view_students'),
                  path('HOD/Student/Edit/<int:id>', HOD_Views.EDIT_STUDENTS, name='edit_students'),
                  path('HOD/Student/Update/<int:id>', HOD_Views.UPDATE_STUDENTS, name='update_students'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
