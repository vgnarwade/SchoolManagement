from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from app.models import CustomUser
from .models import Staff, Subjects
from student.models import Course
from hod.models import StaffNotifications


def staff_home(request):
    return render(request, "staff/staffHome.html")


def staff_list(request):
    staff = Staff.objects.all()

    context = {"staff":staff}
    return render(request, "staff/staffList.html", context)


def staff_details(request, id):
    staff = Staff.objects.get(id=id)

    context = {"staff":staff}
    return render(request, "staff/viewStaff.html", context)


def add_staff(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        contact_no = request.POST.get("contact_no")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        password = request.POST.get("password")
        profile_pic = request.FILES.get("profile_pic")

        # Add CustomUser fields
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists !!!")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email address already exists !!!")
            return redirect("add_staff")

        user = CustomUser(username=username, first_name=first_name, last_name=last_name,
                          email=email, profile_pic=profile_pic, user_type=2)
        user.set_password(password)
        user.save()

        # Add Staff fields
        staff = Staff(admin=user, gender=gender, contact_no=contact_no, address=address)
        staff.save()
        messages.success(request, first_name+" "+ last_name + " 's information added successfully !")
        return redirect("staff_list")

    return render(request, "staff/addStaff.html")


def update_staff(request, id):
    user = CustomUser.objects.get(id=id)
    staff = Staff.objects.get(admin_id=id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        password = request.POST.get("password")
        profile_pic = request.FILES.get("profile_pic")

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        staff.gender = request.POST.get("gender")
        staff.contact_no = request.POST.get("contact_no")
        staff.address = request.POST.get("address")
        staff.updated_at = timezone.now()
        staff.save()
        messages.success(request, "Information updated successfully !")
        return redirect("staff_list")

    context = {"staff":staff}
    return render(request, "staff/updateStaff.html", context)


def delete_staff(request, id):
    staff = CustomUser.objects.get(id=id)
    staff.delete()
    messages.success(request, "Record deleted successfully !")
    return redirect("staff_list")


# Functions for subject

def subject_list(request):
    subjects = Subjects.objects.all()
    context = {"subjects": subjects}
    return render(request, "staff/subjectList.html", context)


def add_subject(request):
    course_ = Course.objects.all()
    staff_ = Staff.objects.all()
    if request.method == "POST":
        subject_name = request.POST.get("s_name")
        course_id = request.POST.get("c_name")
        staff_id = request.POST.get("staff_name")

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subjects(subject_name=subject_name, course=course, staff=staff)
        subject.save()
        messages.success(request, subject_name +" "+ "subject added successfully !")
        return redirect("subject_list")

    context = {"courses":course_, "staff":staff_}
    return render(request, "staff/addSubject.html", context)


def update_subject(request, id):
    course_ = Course.objects.all()
    staff_ = Staff.objects.all()
    subject = Subjects.objects.get(id=id)
    if request.method == "POST":
        subject.subject_name = request.POST.get("s_name")
        course_id = request.POST.get("c_name")
        staff_id = request.POST.get("staff_name")

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        subject.course = course
        subject.staff = staff
        subject.save()
        messages.success(request, "Information updated successfully !")
        return redirect("subject_list")

    context = {"course":course_, "staff":staff_, "subject":subject}
    return render(request, "staff/updateSubject.html", context)


def delete_subject(request, id):
    subject = Subjects.objects.get(id=id)
    subject.delete()
    messages.success(request, "Information deleted successfully !")

    return redirect("subject_list")


# Notifications
def notifications_view(request):
    print("----->", request.user.id)
    staff = Staff.objects.filter(admin=request.user.id)
    for s in staff:

        n_ = StaffNotifications.objects.filter(staff_id=s.id)
        context = {"messages":n_}
    return render(request, "staff/notifications.html", context)


def notifications_read(request, status):
    notifications = StaffNotifications.objects.get(id=status)
    notifications.status = True
    notifications.save()
    return redirect("notifications_viewed")


def staff_apply_leave(request):
    return render(request, "staff/applyLeave.html")






