from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import FileSystemStorage

def index(request):
    blood = request_blood.objects.filter(requester=request.user)
    context = {
        'blood':blood
    }
    return render(request,'index.html',context=context)

def diagnose(request):
    return render(request, 'diagnose.html')

def social_help(request):
    if request.method=='POST':
        if request.FILES['myfile']:
            data = request_blood()
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='media/blood_request')
            filename = fs.save(myfile.name, myfile)
            data.prescription = filename
            data.requester = request.user
            data.unit = request.POST.get('quantity') 
            data.save()
            print(data)
            return redirect('dashboard')
    blood = blood_bank.objects.all()
    context = {
        'blood':blood
    }
    return render(request, 'social-help.html',context=context)

def blog(request):
    return render(request,'blog.html')

