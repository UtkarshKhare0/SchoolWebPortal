from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import School,Student

from django.contrib import messages
from django.urls import reverse

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

def manage_students(request):
    query = request.POST.get("q") or request.GET.get("q")  # search query
    students = []

    if query:
        email = request.POST.get("q") or request.GET.get("q")
        students = Student.objects.filter(student_school_name__icontains=query)

    if request.method == "POST":
        email = request.POST.get("delete") or request.POST.get("update")
        student = get_object_or_404(Student, student_email=email)
        # Delete student
        if "delete" in request.POST:
            student.delete()
            return redirect(f"{reverse('manage_students')}?q={query}")

        # Update student
        elif "update" in request.POST:
            

            # Directly model ke field names le lo
            student.student_name = request.POST.get("student_name", student.student_name)
            student.student_class = request.POST.get("student_class", student.student_class)
            student.student_phone_number = request.POST.get("student_phone_number", student.student_phone_number)
            student.mun_experience = request.POST.get("mun_experience", student.mun_experience)
            student.committee_preference_1 = request.POST.get("committee_preference_1", student.committee_preference_1)
            student.committee_preference_2 = request.POST.get("committee_preference_2", student.committee_preference_2)
            student.alloted_committee = request.POST.get("alloted_committee", student.alloted_committee)
            student.alloted_portfolio = request.POST.get("alloted_portfolio", student.alloted_portfolio)

            student.save()
            return redirect(f"{reverse('manage_students')}?q={query}")

    return render(request, "school_app/school/manage_students.html", {
        "students": students,
        "query": query,
    })


    
