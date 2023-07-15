from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
context={
        'variable': 'vishwa is great'
    }
    
def index(request):
    # return HttpResponse("this is home page")
    messages.success(request,"Refresh for new food")
    return render(request,'index.html',context)
    
def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html',context)
def services(request):
    # return HttpResponse("this is services page")
    return render(request,'services.html',context)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request,'contact.html',context)
