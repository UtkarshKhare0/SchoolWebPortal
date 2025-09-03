from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse("<h1>this is home page</h1>")
    return render(request,'school_app/html/index.html')
