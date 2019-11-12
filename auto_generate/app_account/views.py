from django.shortcuts import render
from .models import Accounts
from  django.views.generic import DetailView


def createAccount(request):
    auto_acno=0
    try:
        res=Accounts.objects.all()[::-1][0]
        auto_acno=int(res.acno)+1
    except IndexError:
        auto_acno=10000006000

    qs=Accounts.objects.all()

    return render(request,'index.html',{'data':auto_acno,'data1':qs})


def employeeRegister(request):
    acno=request.POST.get('acno')
    name=request.POST.get('name')
    actype=request.POST.get('type')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    balance=request.POST.get('balance')
    image=request.FILES["image"]
    res=Accounts(acno=acno,name=name,type=actype,age=age,gender=gender,balance=balance,picture=image)
    res.save()

    return createAccount(request)

class DisplayDetails(DetailView):
    model = Accounts
    template_name = "details.html"
