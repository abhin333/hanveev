from django.shortcuts import render
from hanveevapp.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from genericpath import exists
import os,datetime
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def index(request):
	return render(request,"frontend/index.html")

def about(request):
	return render(request,'frontend/about.html')
#abi--------------------------------------------------------------------

	
def career_view(request):
	tb=careers_register.objects.all()
	return render(request,"frontend/career.html",{"career":tb})

def tender_view(request):
	tb=tender_register.objects.all()
	return render(request,"frontend/tender.html",{"tender":tb})


def contact(request):
	if request.method =='POST':
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		subject=request.POST['subject']
		message=request.POST['message']
		date= datetime.datetime.now().date()
		usermessage = f'Hi {name}, thank you for getting  in touch with us '
		adminmessage= f'message from {name}'+'        '+message
		nsub=f'new messge --[{subject}]'
		con=contact_us(name=name,email=email,phone=phone,subject=subject,message=message,date=date)
		con.save()
		mail_sender( "message recieved", usermessage,email)
		mail_sender(nsub,adminmessage,"tindertapp@gmail.com")
		return render(request,"frontend/contact.html")
	else:
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


def tender_reg(request):
	if request.method == 'POST':
		title= request.POST['title']
		lastdate= request.POST['lastdate']
		timage = request.FILES['timage']
		a=tender_register(title=title,last_date=lastdate,file=timage)
		a.save()
		return  HttpResponseRedirect('/tender_reg/')
	else:
		alll=tender_register.objects.all()
		return render(request, 'backend/tender_reg.html',{'query':alll})


def tender_delete(request):
	if request.session.has_key('adm'):
		tid= request.GET['id']
		tender_register.objects.filter(id=tid).delete()
		return  HttpResponseRedirect('/tender_reg/')
	else:
		return render(request, 'backend/login.html',{'message':'please login'})
   
def tender_update(request):
	if request.method == 'POST':
		tid= request.GET['id']
		title= request.POST['title']
		lastdate= request.POST['lastdate']
		imgup = request.POST['imgup']
		if (imgup == 'yes'):
			image1 = request.FILES['timage']
			oldrec = tender_register.objects.filter(id=tid)
			updrec = tender_register.objects.get(id=tid)
			for x in oldrec:
				imgurl = x.file.url
				pathtoimage = os.path.dirname(
				os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
					updrec.file = image1
					updrec.save()
		tender_register.objects.filter(id=tid).update(title=title,last_date=lastdate)    
		return HttpResponseRedirect('/tender_reg/')    
	else:
		tid= request.GET['id']
		current=tender_register.objects.filter(id=tid)
		alll=tender_register.objects.all()
		return render(request,'backend/tender_update.html',{'up':current,'query':alll})


def career_reg(request):
	if request.method == 'POST':
		od= request.POST['openingdetails']
		lastdate= request.POST['lastdate']
		cimage = request.FILES['cimage']
		a=careers_register(opening_details=od,last_date=lastdate,file=cimage)
		a.save()
		return  HttpResponseRedirect('/career_reg/')
	else:
		alll=careers_register.objects.all()
		return render(request, 'backend/career_reg.html',{'query':alll})

def career_delete(request):
	if request.session.has_key('adm'):
		cid= request.GET['id']
		careers_register.objects.filter(id=cid).delete()
		return  HttpResponseRedirect('/career_reg/')
	else:
		return render(request, 'backend/login.html',{'message':'please login'})


def career_update(request):
	if request.method == 'POST':
		cid= request.GET['id']
		openingdetails= request.POST['openingdetails']
		lastdate= request.POST['lastdate']
		imgup = request.POST['imgup']
		if (imgup == 'yes'):
			image1 = request.FILES['cimage']
			oldrec = tender_register.objects.filter(id=cid)
			updrec = tender_register.objects.get(id=cid)
			for x in oldrec:
				imgurl = x.file.url
				pathtoimage = os.path.dirname(
				os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
					updrec.file = image1
					updrec.save()
		careers_register.objects.filter(id=cid).update(opening_details=openingdetails,last_date=lastdate)    
		return HttpResponseRedirect('/career_reg/')    
	else:
		cid= request.GET['id']
		current=careers_register.objects.filter(id=cid)
		alll=careers_register.objects.all()
		return render(request,'backend/career_update.html',{'up':current,'query':alll})

def news(request):
	if request.method == 'POST':
		newnews= request.POST['addnews']
		a=news_lines(description=newnews)
		a.save()
		return HttpResponseRedirect('/news/')
	else:
		alll=news_lines.objects.all()
		return render(request, 'backend/news.html',{'query':alll})


def newsdelete(request):
	if request.session.has_key('adm'):
		nid= request.GET['id']
		news_lines.objects.filter(id=nid).delete()
		return HttpResponseRedirect('/news')
	else:
		return render(request, 'backend/login.html',{'message':'please login'})


def mail_sender(subject,message, recipient):
	email_from =  settings.EMAIL_HOST_USER 
	recipient_list = [recipient, ] 
	send_mail( subject, message, email_from, recipient_list )
#vishnu------------------------------------------------