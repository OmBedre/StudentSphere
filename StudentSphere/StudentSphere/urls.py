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
                  path('HOD/Student/Edit/<str:id>', HOD_Views.EDIT_STUDENTS, name='edit_students'),
                  path('HOD/Student/Update', HOD_Views.UPDATE_STUDENTS, name='update_students'),
                  path('HOD/Student/Delete/<str:admin>', HOD_Views.DELETE_STUDENTS, name='delete_students'),

                  path('HOD/Course/Add', HOD_Views.ADD_COURSES, name='add_courses'),
                  path('HOD/Course/View', HOD_Views.VIEW_COURSES, name='view_courses'),
                  path('HOD/Course/Edit/<str:id>', HOD_Views.EDIT_COURSE, name='edit_course'),
                  path('HOD/Course/Update', HOD_Views.UPDATE_COURSE, name='update_course'),
                  path('HOD/Course/Delete/<str:id>', HOD_Views.DELETE_COURSE, name='delete_course'),

                  path('HOD/Staff/Add', HOD_Views.ADD_STAFF, name='add_staff'),
                  path('HOD/Staff/View', HOD_Views.VIEW_STAFF, name='view_staff'),
                  path('HOD/Staff/Edit/<str:id>', HOD_Views.EDIT_STAFF, name='edit_staff'),
                  path('HOD/Staff/Delete/<str:admin>', HOD_Views.DELETE_STAFF, name='delete_staff'),
                  path('HOD/Staff/Update/<str:id>', HOD_Views.UPDATE_STAFF, name='update_staff'),

                  path('HOD/Subject/Add', HOD_Views.ADD_SUBJECT, name='add_subject'),
                  path('HOD/Subject/View', HOD_Views.VIEW_SUBJECT, name='view_subject'),
                  path('HOD/Subject/Edit/<str:id>', HOD_Views.EDIT_SUBJECT, name='edit_subject'),
                  path('HOD/Subject/Update', HOD_Views.UPDATE_SUBJECT, name='update_subject'),
                  path('HOD/Subject/Delete/<str:id>', HOD_Views.DELETE_SUBJECT, name='delete_subject'),

                  path('HOD/Session/Add', HOD_Views.ADD_SESSION, name='add_session'),
                  path('HOD/Session/View', HOD_Views.VIEW_SESSIONS, name='view_sessions'),
                  path('HOD/Session/Edit/<str:id>', HOD_Views.EDIT_SESSION, name='edit_session'),
                  path('HOD/Session/Delete/<str:id>', HOD_Views.DELETE_SESSION, name='delete_session'),
                  path('HOD/Session/Update', HOD_Views.UPDATE_SESSION, name='update_session'),
                  path('HOD/Staff/Send_Notifications', HOD_Views.SEND_STAFF_NOTIFICATION,
                       name='send_staff_notification'),
                  path('HOD/Staff/Save_Notifications', HOD_Views.SAVE_STAFF_NOTIFICATION,
                       name='save_staff_notification'),
                  path('HOD/Staff/Leave_Applied', HOD_Views.STAFF_LEAVE_APPLIED_VIEW, name='staff_leave_applied_view'),
                  path('HOD/Staff/Approve_Leave/<str:id>', HOD_Views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
                  path('HOD/Staff/Disapprove_Leave/<str:id>', HOD_Views.STAFF_DISAPPROVE_LEAVE,
                       name='staff_disapprove_leave'),


                  #     Staff Panel      #
                  path('Staff/Home', Staff_Views.HOME, name='staff_home'),
                  path('Staff/Notifications', Staff_Views.NOTIFICATIONS, name='staff_notifications'),
                  path('Staff/Notification/Mark_as_Done/<str:status>', Staff_Views.Mark_as_Done, name="mark_as_done"),
                  path('Staff/Apply_Leave', Staff_Views.LEAVE_APPLICATION, name='staff_apply_leave'),
                  path('Staff/Apply_Leave_Save', Staff_Views.LEAVE_APPLY_SAVE, name='staff_leave_apply_save'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
