from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import Students, Course, SessionYear
from staff.models import Staff, Subjects
from .models import StaffNotifications, StaffLeave, StaffFeedback, StudentNotifications


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
        staff_ = Staff.objects.get(admin=staff_id)
        notification = StaffNotifications(staff=staff_, message=message_)
        notification.save()
        messages.success(request, "Notification sent successfully !")

    return redirect("send_staff_notification")


def view_staff_leaves(request):
    leaves = StaffLeave.objects.all()

    context = {"leaves":leaves}
    return render(request, "hod/viewStaffLeaves.html", context)


def approve_staff_leave(request, id):
    leave = StaffLeave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect("view_staff_leaves")


def disapprove_staff_leave(request, id):
    leave = StaffLeave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect("view_staff_leaves")


def staff_feedback(request):
    feedback = StaffFeedback.objects.all()
    staff = Staff.objects.all()
    context = {"feedbacks":feedback, "staffs":staff}
    return render(request, "hod/ViewFeedbacks.html", context)


def reply_to_staff_feedback(request):
    if request.method == "POST":
        feedback_id = request.POST.get("feedback_id")
        print("-------->", id)
        reply = StaffFeedback.objects.get(id=feedback_id)
        feedback = request.POST.get("feedback_reply")
        reply.feedback_reply = feedback
        reply.save()
        messages.success(request, "Reply sent successfully !")
        return redirect("staff_feedbacks")
    return render("hod/replyStaffFeedback.html")


def student_notifications(request):
    students = Students.objects.all()
    notify = StudentNotifications.objects.all()[0:5]

    context = {"students":students, "notify":notify}
    return render(request, "hod/sendStudentNotification.html", context)


def save_student_notification(request):
    if request.method == "POST":
        message = request.POST.get("message")
        student_id = request.POST.get("student_id")
        student = Students.objects.get(admin=student_id)

        notification = StudentNotifications(message=message, student=student)
        notification.save()
        messages.success(request, "Notification is sent to student.")
        return redirect("student_notification")
    return render(request, "hod/sendStudentNotification.html")


