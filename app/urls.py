from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # Update Profile
    path("update-profile/", views.update_profile, name="update_profile"),


]