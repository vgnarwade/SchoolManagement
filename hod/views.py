from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import Students, Course, SessionYear
from staff.models import Staff, Subjects
from .models import StaffNotifications


@login_required
def hod_home(request):
    student_count = Students.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subjects.objects.all().count()
    staff_count = Staff.objects.all().count()

    student_girls = Students.objects.filter(gender="Female").count()
    student_boys = Students.objects.filter(gender="Male").count()

    context = {"student_count":student_count,
               "course_count":course_count,
               "subject_count":subject_count,
               "staff_count":staff_count,
               "student_girls":student_girls,
               "student_boys":student_boys,
               }
    return render(request, "hod/hodHome.html", context)


def send_staff_notification(request):
    staff = Staff.objects.all()
    msg = StaffNotifications.objects.all().order_by()[0:5]
    context = {"staff":staff, "messages":msg}
    return render(request, "hod/staffNotification.html", context)


def save_staff_notification(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        message_ = request.POST.get("message")
        print("------>", staff_id)
        staff_ = Staff.objects.get(admin=staff_id)
        notification = StaffNotifications(staff=staff_, message=message_)
        notification.save()
        messages.success(request, "Notification sent successfully !")

    return redirect("send_staff_notification")


