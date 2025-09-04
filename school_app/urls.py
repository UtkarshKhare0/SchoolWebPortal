from django.urls import path, include
from .import views,student_views
urlpatterns = [
    
    path("",views.home,name="home"),

    path("register/",student_views.register_student,name="register_student"),
    path("login/",student_views.login_student,name="login_student")
]