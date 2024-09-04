from django.urls import path
from . import views


urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("student-details/<int:id>/", views.view_student, name="student_details"),
    path("add-student/", views.add_student, name="add_student"),
    path("update-student/<int:id>/", views.update_student, name="update_student"),
    path("delete-student/<int:admin>/", views.delete_student, name="delete_student"),

    # Course urls
    path("courses/", views.course_list, name="course_list"),
    path("add-course/", views.add_course, name="add_course"),
    path("update-course/<int:id>/", views.update_course, name="update_course"),
    path("delete-course/<int:id>/", views.delete_course, name="delete_course"),

    # Session urls
    path("sessions/", views.session_list, name="session_list"),
    path("add-session/", views.add_session, name="add_session"),
    path("update-session/<int:id>/", views.update_session, name="update_session"),
    path("delete-session/<int:id>/", views.delete_session, name="delete_session"),


]