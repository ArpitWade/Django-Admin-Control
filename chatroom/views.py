from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import models

# Create your views here.
def home(request):
    obj = models.layout.objects.all()
    return render(request,"base.html",{'obj':obj})
    #return HttpResponse('Home')


def contact(request):
    n=""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('tel')
        desc = request.POST.get('desc')
        obj = models.Contact(Name=name, Email=email, Phone=phone, Description=desc)
        obj.save()
        n+="Registered Successfully"

    return render(request,'contact.html',{'register':n})


def Sweet(request):
    n=""
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        contact = request.POST.get('Contact')
        desc = request.POST.get('suggestions')
        res = models.Contact(Name = name, Email = email, Phone = contact, Description = desc)
        res.save()

        n+="Registered Successfully"
        url="/thanks/?output={}".format(name)
        return redirect(url)
    return render(request,'SweetCake.html')

def Orders(request):
    obj = models.Products.objects.all()
    return render(request,'Orders.html',{'obj':obj})


def thanks(request):
    name_get=""
    if request.method == 'GET':
        name_get = request.GET.get('output')
    return render(request,'thanks.html',{'fullname':name_get})


def chating(request):
    return render(request,'base.html')

def room(request):
    return HttpResponse("Room")