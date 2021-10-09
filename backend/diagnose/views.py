from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def diagnose(request):
    return render(request, 'diagnose.html')

def social_help(request):
    return render(request, 'social-help.html')

def blog(request):
    return render(request,'blog.html')

