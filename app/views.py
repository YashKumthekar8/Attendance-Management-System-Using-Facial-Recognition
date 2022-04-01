from cmath import log
from email import message
import imp
from multiprocessing import AuthenticationError
from traceback import print_tb
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import append
from app.models import *
from .model_form import *
from .utility import *
from .ImageCapture import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
import pandas as pd
import os
from graphs import *
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from graphs import *	


#For Registering New User on Admin Page
@login_required
def Signup(request):
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
				form.save()
				obj=User.objects.get(username=request.POST.get('username'))
				fm=ImageForm()
				return render(request,'Signup.html',context={'form':fm,"name":obj.id,'id':2})

		if "upload" in request.POST:
			form=ImageForm(request.POST,request.FILES)		
			form.save()
			return redirect('Home')

		else:
			if request.method=="POST":
				form=UserCreationForm()
				return render(request,'Signup.html',context={'form':form,"message":"Please Enter Correct Details",'id':1})

			else:		
				form=UserCreationForm()
				return render(request,'Signup.html',context={'form':form,'id':1})


#FOR Main Login Page
def home(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():

			auth=authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
			login(request,auth)
			obj = User.objects.get(username = request.POST.get('username'))
			
			#IF admin redirecting to admin page
			if obj.is_superuser:
            		    return redirect('Admin')
			else:
						return redirect(f"user/{request.POST.get('username')}")

		else:
			form=AuthenticationForm()
			return render(request,'login.html',context={'form':form,"message":"Please Enter Valid Username and Password"})

	else:
		form=AuthenticationForm()
		return render(request,'login.html',context={'form':form})


#FOR UPLOADING GROUP IMAGE In Admin Page
@login_required
def upload(request):
			form = AttendanceForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()

				ImgPath=""
				dir = 'media/unknown'
				for f in os.listdir(dir):
					ImgPath=f"{dir}/{f}"

				
				photo_name=Recognize(ImgPath)
				q=Image.objects.all()
				name=[]
				for i in q:
					if str(i.person_Img.path.split('\\')[-1]) in photo_name:
						name.append(i.name)
				message=""		
				if len(name)==0:
					message="Nobody present"
				else:
					message="Students present are "
					for i in name:
							att=Attendance(user=i,time=request.POST.get('time'))
							att.save()
							message=message+str(i)+" "
                
				form = AttendanceForm()
				return render(request, 'Upload.html', {'form' : form,'message':message})

 

			else:
				form = AttendanceForm()
				return render(request, 'Upload.html', {'form' : form})




#For rendering the Admin Page
@login_required
def admin(request):
	return render(request, 'Admin.html')

#For user page and capturing the photo of user for attendance
@login_required
def UsersPage(request,name):
	if request.method=='POST':
				
		CaptureImage(name)
		ImgPath=""
		dir = 'media/unknown'
		for f in os.listdir(dir):
			ImgPath=f"{dir}/{f}"
        
		photo_name=Recognize(ImgPath)
		q=Image.objects.all()
		names=[]
		for i in q:
			if str(i.person_Img.path.split('\\')[-1]) in photo_name:
				names.append(i.name)
		message=""
		if len(names)!=0:
			    #Marking the attendance of current user in dataabse
				now = datetime.now()
				current_time = now.strftime("%H:%M:%S")
				obj=User.objects.get(username=name)
				att=Attendance(user=obj,time=current_time)
				att.save()
				message="Your Attendance is marked Succesfully" 		
		else:
			message="There was an issue please try again"

		for f in os.listdir(dir):
			os.remove(os.path.join(dir, f))

		return render(request,'User.html',context={'message':message,'name':name})	
	else:
	   return render(request,'User.html',context={'name':name})




#Function for the count graph
def CountGraph(dates,intime,outtime):
	obj=Attendance.objects.all()
	present=[]
	for i in dates:
		count=0
		for j in obj:
			if j.date==i and str(j.time)>=intime and str(j.time)<=outtime:
				count=count+1
		temp=[]
		temp.append(i)
		temp.append(count)
		present.append(temp) 

	return pd.DataFrame(present,columns=["dates","count"])  


#Function for the student graph
def StudentGraph(dates,intime,outtime,name):
	obj=Attendance.objects.all()
	present=[]
	for i in dates:
		count=0
		for j in obj:
			if j.date==i and str(j.time)>=intime and str(j.time)<=outtime and str(j.user)==name :
				count=1
		temp=[]
		temp.append(i)
		temp.append(count)
		present.append(temp) 

	return pd.DataFrame(present,columns=["dates","count"])  



#Function for the admin reports page
@login_required
def AdminReports(request):
	if request.method=="POST":
		obj=User.objects.all()
		usernames=[]
		for i in obj:
			if not i.is_superuser: 
				usernames.append(str(i.username))


		#Code for the count graph
		if  "graph1" in request.POST:

			intime=request.POST.get('intime')
			outtime=request.POST.get('outtime')

			#Throwing message if intime>=outtime
			if intime>=outtime:
				return render(request,'admin_report.html',context={'message1':"Lecture start time cannot be greater than and equal to lecture end time",'name':usernames})	
			
			temp=str(request.POST.get('week'))
			year=int(temp.split('-')[0])
			weekNo=temp[-2:]

			dates=weekNoToDates(year,int(weekNo))
			dataGraph=CountGraph(dates,intime,outtime)
			graph=BarGraph(dataGraph)
			

			return render(request,'admin_report.html',context={'name':usernames,'graph1':graph})
		
		
		elif "graph2" in request.POST:
			
			intime=request.POST.get('intime1')
			outtime=request.POST.get('outtime1')

			#Throwing message if intime>=outtime
			if intime>=outtime:
				return render(request,'admin_report.html',context={'message2':"Lecture start time cannot be greater than and equal to lecture end time",'name':usernames})	
			
			name=request.POST.get('student')
			my_date = datetime.now() 
			year, week_num, day_of_week = my_date.isocalendar()
			dates=weekNoToDates(int(year),int(week_num))
			dataGraph=StudentGraph(dates,intime,outtime,name)
			graph=BarGraph(dataGraph)
			return render(request,'admin_report.html',context={'name':usernames,'graph2':graph})


	else:	
		return render(request,'admin_report.html',context={'name':usernames})



#Function for the user reports page
def UserReports(request,name):
	if request.method=="POST":
		intime=request.POST.get('intime')
		outtime=request.POST.get('outtime')

		#Throwing message if intime>=outtime
		if intime>=outtime:
			return render(request,'admin_report.html',context={'message1':"Lecture start time cannot be greater than and equal to lecture end time"})	
		
		temp=str(request.POST.get('week'))
		year=int(temp.split('-')[0])
		weekNo=temp[-2:]

		dates=weekNoToDates(year,int(weekNo))
		dataGraph=StudentGraph(dates,intime,outtime,name)
		graph=BarGraph(dataGraph)
		return render(request,'user_report.html',context={'graph':graph,'intime':intime,'outtime':outtime,'week':temp})

	else:	
	  return render(request,'user_report.html')

