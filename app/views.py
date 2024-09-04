from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser


def login_page(request):
    try:
        request.session["login_id"]
        return redirect("dashboard")
    except:
        pass
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == "1":
                return redirect("/hod/hod-home/")
            elif user_type == "2":
                return redirect("staff_home")
            else:
                return HttpResponse("This is STUDENT page.")
        else:
            messages.error(request, "Invalid username or password !!!")
            return redirect("login_page")
    return render(request, "login/loginPage.html")


def logout_page(request):
    logout(request)
    return redirect("/")


def dashboard(request):
    return render(request, "base.html")


def update_profile(request):
    if request.method == "POST":
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            # customuser.username = request.POST.get("username")
            customuser.first_name = request.POST.get("first_name")
            customuser.last_name = request.POST.get("last_name")
            # customuser.email = request.POST.get("email")
            profile_pic = request.FILES.get("profile_pic")
            password = request.POST.get("password")

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            if password != None and password != "":
                customuser.set_password(password)

            customuser.save()
            messages.success(request, "Your profile updated successfully !")
            return redirect("update_profile")
        except:
            messages.error(request, "Failed to update your profile !!!")

    user = CustomUser.objects.get(id=request.user.id)
    context = {"user":user}
    return render(request, "profile.html", context)

