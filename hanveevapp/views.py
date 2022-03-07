from django.shortcuts import render
from hanveevapp.models import *
from django.contrib.auth.models import User


# Create your views here.

def index(request):
	return render(request,"frontend/index.html")

def about(request):
	return render(request,'frontend/about.html')
#abi--------------------------------------------------------------------

	
def career_reg(request):
	if request.method=='POST':
		opening_details=request.POST['opening_details']
		last_date=request.POST['last_date']
		file=request.FILE['file']
		tb=careers_register(opening_details=opening_details,last_date=last_date,file=file)
		tb.save()
		return render(request,"career_reg.html")
	else:
		return render(request,"career_reg.html")

def tender(request):
	if request.method=='POST':
		title=request.POST['title']
		last_date=request.POST['last_date']
		file=request.FILE['file']
		tb=tender_register(titile=title,last_date=last_date,file=file)
		tb.save()
		return render(request,"tender_reg.html")
	else:
		return render(request,"tender_reg.html")




def contact(request):
	return render(request,"frontend/contact.html")


def ga(request):
	return render(request,"frontend/gallery.html")







#------------------------------------------------------------------------

#vishnu------ADMIN-----------------------------------------

def admin_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		use = User.objects.filter(username=username, password=password)
		if use:
			for x in use:
				name = x.username
				pswd = x.password
				if username == name and password == pswd:
					request.session['adm'] = x.id
					return render(request, 'backend/homepage.html',{'message': 'successfully logged in', })
				else:
					return render(request, 'backend/login.html',{'message': 'invalid credentials'})
		else:
			return render(request, 'backend/login.html',{'message': 'invalid credentials'})
	else:
		return render(request, 'backend/login.html')


def admin_logout(request):
    if request.session.has_key('adm'):
        del request.session['adm']
    return render(request, 'backend/login.html')


def homepage(request):
    if request.session.has_key('adm'):
        return render(request, 'backend/homepage.html')
    else:
        return render(request, 'backend/login.html',{'message':'please login'})

def brands(request):
	return render(request,'backend/brands.html')

def user(request):
	return render(request, 'backend/user.html')


def category(request):
	return render(request, 'backend/category.html')


def products(request):
	return render(request, 'backend/products.html')


def gallery(request):
	return render(request, 'backend/gallery.html')


def contactus(request):
	return render(request, 'backend/contactus.html')


def getprice(request):
	return render(request, 'backend/getprice.html')

def newsletter(request):
	return render(request, 'backend/newsletter.html')

#vishnu------------------------------------------------