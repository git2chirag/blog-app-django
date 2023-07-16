from django.shortcuts import render
from django.http import HttpResponse

posts=[{'author':'DSPAPLU','title':'blog posts','content':'First Post content','date':'9/11'},{'author':'tom jerry','title':'FUN and GAmes','content':'2nd Post content','date':'26/11'}] #dummy data

def home(request):
    context={'posts':posts} #setting up posts
    return render(request,'blog/home.html',context) # using render function instead of http response

def about(request):
    return render(request,'blog/about.html',{'title':'ABOUT'})
# Create your views here.
