from django.db import models
from app.models import CustomUser


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


class SessionYear(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_start + " to " + self.session_end


class Students(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    contact_no = models.CharField(max_length=20)
    address = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(SessionYear, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

