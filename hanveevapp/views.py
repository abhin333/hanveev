from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,"frontend/index.html")

def adminlogin(request):
	return render(request,'backend/login.html')