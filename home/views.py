from django.shortcuts import render,HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages

def index(request):
    
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def about(request):
    return render(request,'aboutus.html')
def gallery(request):
    return render(request,'gallery.html')
def contactus(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email = email,phone = phone,desc= desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent')
    return render(request,'contact.html')
def gymnastic(request):
    return render(request,'gymnastic.html')
def calisthenic(request):
    return render(request,'calisthenic.html')

