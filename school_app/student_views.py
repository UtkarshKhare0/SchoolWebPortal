from django.shortcuts import render,HttpResponse,redirect
from .models import Student

from django.contrib import messages

def register_student(request):

    if request.method=="GET":
        return render (request, 'school_app/student/student_registration.html',{"committee_choices":Student.COMMITTEE_CHOICES})
    
    if request.method=="POST":
        reg_name = request.POST["student_name"]
        reg_class = request.POST["student_class"]
        reg_phone = request.POST["student_phone_number"]
        reg_email = request.POST["student_email"]
        reg_pass = request.POST["student_password"]
        reg_experience = request.POST["mun_experience"]
        reg_pref_1 = request.POST["committee_preference_1"]
        reg_pref_2 = request.POST["committee_preference_2"]
        reg_head = request.POST.get("is_head_delegate") == "on"
        reg_inname = request.POST["incharge_name"]
        reg_inphone = request.POST["incharge_phone_number"]
        reg_inemail = request.POST["incharge_email"]

        student_registration_obj = Student(
            student_name = reg_name,
            student_class = reg_class,
            student_phone_number = reg_phone,
            student_email = reg_email,
            student_password = reg_pass,
            mun_experience = reg_experience,
            committee_preference_1 = reg_pref_1,
            committee_preference_2 = reg_pref_2,
            is_head_delegate = reg_head,
            incharge_name = reg_inname,
            incharge_phone_number = reg_inphone,
            incharge_email = reg_inemail
        )
        student_registration_obj.save()
        messages.success(request, "Registration Successful! Please Login.")
        return redirect("login_student")

def login_student(request):
    if request.method=="GET":
        return render(request, 'school_app/student/student_login.html')
    
    if request.method=="POST":
        email = request.POST["student_email"]
        password = request.POST["student_password"]
        studentList = Student.objects.filter(student_email=email,student_password=password)
        if studentList.exists():
            request.session["student_key"] = email
            messages.success(request, "Login Successful! Welcome Back.")
            return redirect("dashboard_student")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login_student")

def logout_student(request):
    request.session.flush()
    messages.success(request,"Logged Out Successfully!")
    return redirect("login_student")

def dashboard_student(request):
    if request.method=="GET":
        email = request.session["student_key"]
        student_obj = Student.objects.get(student_email=email)
        student_dict = {"student":student_obj}
        return render(request,'school_app/student/student_dashboard.html',student_dict)
    
def edit_profile_student(request):
    if request.method=="GET":
        email = request.session["student_key"]
        student_obj = Student.objects.get(student_email=email)
        student_dict = {"student":student_obj}
        return render(request,'school_app/student/student_edit_profile.html',student_dict)
    if request.method=="POST":
        email = request.session["student_key"]
        student_obj = Student.objects.get(student_email=email)
        new_name = request.POST["student_name"]
        new_class = request.POST["student_class"]
        new_password = request.POST["student_password"]
        new_phone = request.POST["student_phone_number"]

        if new_name:
            student_obj.student_name = new_name
        if new_class:
            student_obj.student_class = new_class
        if new_password:
            student_obj.student_password = new_password
        if new_phone:
            student_obj.student_phone_number = new_phone
        student_obj.save()
        messages.success(request,"Profile Updated Successfully!")
        return redirect("dashboard_student")




    