from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HOD_Views,Staff_Views,Students_Views



urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('base/', views.BASE, name='base'),

                    path('', views.LOGIN, name='login'),
                    path('doLogin/',views.doLogin, name= 'doLogin'),
                    path('doLogout/',views.doLogout, name= 'logout'),

                    path('profile/', views.PROFILE, name='profile'),
                    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

                    path('HOD/home',HOD_Views.home, name='HOD_home'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
