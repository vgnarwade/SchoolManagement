from django.urls import path
from . import views


urlpatterns = [
    path("hod-home/", views.hod_home, name="hod_home"),
    path("staff-notification/", views.send_staff_notification, name="send_staff_notification"),
    path("save-staff-notification/", views.save_staff_notification, name="save_staff_notification"),

]