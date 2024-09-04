from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from .models import Students, Course, SessionYear


@login_required(login_url="/")
def student_list(request):
    students = Students.objects.all().order_by("-updated_at")

    context = {"students":students}
    return render(request, "student/studentList.html", context)


@login_required(login_url="/")
def view_student(request, id):
    students = Students.objects.get(id=id)
    context = {"student":students}
    return render(request, "student/viewStudent.html", context)


@login_required(login_url="/")
def add_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        contact_no = request.POST.get("contact_no")
        address = request.POST.get("address")
        course = request.POST.get("course")
        session = request.POST.get("session_year")
        profile_pic = request.POST.get("profile_pic")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists !!!")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists !!!")
            return redirect("add_student")
        else:
            # Add user data
            user = CustomUser(username=username, first_name=first_name, last_name=last_name,
                              email=email, profile_pic=profile_pic, user_type=3)
            user.set_password(password)
            user.save()

        course_id = Course.objects.get(id=course)
        session_id = SessionYear.objects.get(id=session)

        # Add student
        student = Students(admin=user, dob=dob, gender=gender, contact_no=contact_no,address=address,
                           course_id=course_id, session_year_id=session_id)
        student.save()
        messages.success(request, user.first_name+" "+user.last_name+ "'s information added successfully.")
        return redirect("student_list")

    courses = Course.objects.all()
    sessions = SessionYear.objects.all()

    context = {"courses":courses, "session_year":sessions}
    return render(request, "student/addStudent.html", context)


@login_required(login_url="/")
def update_student(request, id):
    student = Students.objects.get(admin_id=id)
    user = CustomUser.objects.get(id=id)

    if request.method == "POST":
        # Update user data
        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        profile_pic = request.FILES.get("profile_pic")
        password = request.POST.get("password")

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)

        user.save()

        # Update student data
        course_id = request.POST.get("course")
        session_year = request.POST.get("session_year")

        course = Course.objects.get(id=course_id)
        session = SessionYear.objects.get(id=session_year)

        student.gender = request.POST.get("gender")
        if request.POST.get("dob"):
            student.dob = request.POST.get("dob")
        student.contact_no = request.POST.get("contact_no")
        student.address = request.POST.get("address")
        student.course_id = course
        student.session_year_id = session
        student.updated_at = timezone.now()

        student.save()
        messages.success(request, "Student information updated successfully.")
        return redirect("student_list")

    courses = Course.objects.all()
    session_years = SessionYear.objects.all()

    context = {"stud": student, "courses": courses, "session_years": session_years}
    return render(request, "student/updateStudent.html", context)


@login_required(login_url="/")
def delete_student(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, "Student information deleted successfully !")
    return redirect("student_list")


# Course related views

def course_list(request):
    course_ = Course.objects.all()
    context = {"courses":course_}
    return render(request, "hod/courseList.html", context)


def add_course(request):
    if request.method == "POST":
        course = request.POST.get("course_name")
        new_course = Course(course_name=course)
        new_course.save()
        messages.success(request, "Course added successfully !")
        return redirect("course_list")
    return render(request, "hod/addCourse.html")


def update_course(request, id):
    course = Course.objects.get(id=id)

    if request.method == "POST":
        course.course_name = request.POST.get("course_name")
        course.updated_at = timezone.now()
        course.save()
        messages.success(request, "Course updated successfully !")
        return redirect("course_list")

    context = {"course":course}
    return render(request, "hod/updateCourse.html", context)


def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Course deleted successfully !")
    return redirect("course_list")


# Session related views
def session_list(request):
    sessions = SessionYear.objects.all()

    context = {"sessions":sessions}
    return render(request, "hod/sessionList.html", context)


def add_session(request):
    if request.method == "POST":
        start = request.POST.get("start")
        end = request.POST.get("end")

        session = SessionYear(session_start=start, session_end=end)
        session.save()
        messages.success(request, "Session-year added successfully !")
        return redirect("session_list")

    return render(request, "hod/addSession.html")


def update_session(request, id):
    session = SessionYear.objects.get(id=id)
    if request.method == "POST":
        session.session_start = request.POST.get("start")
        session.session_end = request.POST.get("end")
        session.save()
        messages.success(request, "Session-year updated successfully ")
        return redirect("session_list")

    context = {"s":session}
    return render(request, "hod/updateSession.html", context)


def delete_session(request, id):
    session = SessionYear.objects.get(id=id)
    session.delete()
    messages.success(request, "Session-year deleted successfully !")
    return redirect("session_list")









