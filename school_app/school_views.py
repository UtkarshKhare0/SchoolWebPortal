from django.shortcuts import render,HttpResponse,redirect
from .models import School

from django.contrib import messages

def register_school(request):

    if request.method=="GET":
        return render(request,'school_app/school/school_registration.html')
    
    if request.method=="POST":
        reg_name = request.POST["school_name"]
        reg_class = request.POST["school_class"]
        reg_design = request.POST["school_designation"]
        reg_phone = request.POST["school_phone_number"]
        reg_email = request.POST["school_email"]
        reg_pass = request.POST["school_password"]

        school_registration_obj = School(
            school_name = reg_name,
            school_class = reg_class,
            school_designation = reg_design,
            school_phone_number = reg_phone,
            school_email = reg_email,
            school_password = reg_pass
        )
        school_registration_obj.save()
        messages.success(request,"Registration Successfull! Please Login.")
        return redirect("login_school")
    
def login_school(request):

    if request.method=="GET":
        return render(request,'school_app/school/school_login.html')
    
    if request.method=="POST":
        email = request.POST["school_email"]
        password = request.POST["school_password"]
        schoolList = School.objects.filter(school_email=email,school_password=password)
        if schoolList.exists():
            request.session["school_key"] = email
            messages.success(request,"Login Successful! Welcome Back.")
            return redirect("dashboard_school")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login_school")
        
def logout_school(request):
    request.session.flush()
    messages.success(request,"Logged Out Successfully!")
    return redirect("login_school")

def dashboard_school(request):
    if request.method=="GET":
        email = request.session["school_key"]
        school_obj = School.objects.get(school_email=email)
        school_dict = {"school":school_obj}
        return render(request,'school_app/school/school_dashboard.html',school_dict)
    
def edit_profile_school(request):
    if request.method=="GET":
        email = request.session["school_key"]
        school_obj = School.objects.get(school_email=email)
        school_dict = {"school":school_obj}
        return render(request,'school_app/school/school_edit_profile.html',school_dict)
    if request.method=="POST":
        email = request.session["school_key"]
        school_obj = School.objects.get(school_email=email)
        new_name = request.POST["school_name"]
        new_password = request.POST["school_password"]
        new_class = request.POST["school_class"]
        new_design = request.POST["school_designation"]
        new_phone = request.POST["school_phone_number"]

        if new_name:
            school_obj.school_name = new_name
        if new_password:
            school_obj.school_password = new_password
        if new_class:
            school_obj.school_class = new_class
        if new_design:
            school_obj.school_designation = new_design
        if new_phone:
            school_obj.school_phone_number = new_phone
        school_obj.save()
        messages.success(request,"Profile Updated Successfully!")
        return redirect("dashboard_school")
    

    
