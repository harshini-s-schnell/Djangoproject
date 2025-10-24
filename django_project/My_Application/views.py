from django.shortcuts import render
from django.http import HttpResponse
from My_Application.models import datas


# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']
        obj=datas()
        obj.name=name
        obj.age=age
        obj.address=address
        obj.contact=contact
        obj.mail=mail
        obj.save()
        mydata=datas.objects.all()
        return render(request,'home.html',{'datas':mydata})
    return render(request,'home.html')
