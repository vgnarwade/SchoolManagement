from django.urls import path
from . import views


urlpatterns = [
    path("hod-home/", views.hod_home, name="hod_home"),

    # Staff notifications
    path("staff-notification/", views.send_staff_notification, name="send_staff_notification"),
    path("save-staff-notification/", views.save_staff_notification, name="save_staff_notification"),

    # Staff leave
    path("view-staff-leave/", views.view_staff_leaves, name="view_staff_leaves"),
    path("approve-staff-leave/<int:id>/", views.approve_staff_leave, name="approve_staff_leave"),
    path("disapprove-staff-leave/<int:id>/", views.disapprove_staff_leave, name="disapprove_staff_leave"),

    # Staff feedback
    path("staff-feedbacks/", views.staff_feedback, name="staff_feedbacks"),
    path("staff-feedback-reply/", views.reply_to_staff_feedback, name="staff_feedback_reply"),

    # Student urls
    path("student-notification/", views.student_notifications, name="student_notification"),
    path("save-student-notification/", views.save_student_notification, name="save_student_notification"),



]