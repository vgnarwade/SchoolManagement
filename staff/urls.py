from django.urls import path
from . import views


urlpatterns = [
    path("staff-home/", views.staff_home, name="staff_home"),
    path("staffs/", views.staff_list, name="staff_list"),
    path("add-staff/", views.add_staff, name="add_staff"),
    path("staff-details/<int:id>/", views.staff_details, name="staff_details"),
    path("update-staff/<int:id>/", views.update_staff, name="update_staff"),
    path("delete-staff/<int:id>/", views.delete_staff, name="delete_staff"),

    # Urls for subjects
    path("subjects/", views.subject_list, name="subject_list"),
    path("add-subject/", views.add_subject, name="add_subject"),
    path("update-subject/<int:id>/", views.update_subject, name="update_subject"),
    path("delete-subject/<int:id>/", views.delete_subject, name="delete_subject"),

    # Url for notifications
    path("view-staff-notifications/", views.notifications_view, name="notifications_viewed"),
    path("read-staff-notification/<str:status>/", views.notifications_read, name="notifications_read"),
    path("apply-leave/", views.staff_apply_leave, name="staff_apply_leave"),




]