from django.urls import path, include
from .import views,student_views,school_views
urlpatterns = [
    
    path("",views.home,name="home"),

    path("register/",student_views.register_student,name="register_student"),
    path("login/",student_views.login_student,name="login_student"),
    path("dashboard/",student_views.dashboard_student,name="dashboard_student"),
    path("edit-profile/",student_views.edit_profile_student,name="edit_profile_student"),
    path("logout/",student_views.logout_student,name="logout_student"),

    path("school_register/",school_views.register_school,name="register_school"),
    path("school_login/",school_views.login_school,name="login_school")
]