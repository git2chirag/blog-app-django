from django.shortcuts import render
from django.http import HttpResponse
from .models import post


def home(request):
    context={'posts':post.objects.all()} #setting up posts
    return render(request,'blog/home.html',context) # using render function instead of http response

def about(request):
    return render(request,'blog/about.html',{'title':'ABOUT'})
# Create your views here.
