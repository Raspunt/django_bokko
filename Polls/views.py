from django.shortcuts import render
from django.http import HttpResponse
from Polls.models import Student, Student_cource


def MainPage(request):
    return render(request,"polls/UserProfile.html")

def LoginPage(request):

    print(request.POST)

    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password_user")
        email = request.POST.get("email_user")
        phone_number = request.POST.get("phone_number_user")


    return render(request,"polls/login.html")




def RegisterPage(request):

    sc =  Student_cource.objects.all()

    print(request.POST)


    return render(request,"polls/reg.html",
    {
        "cources":sc
    })


