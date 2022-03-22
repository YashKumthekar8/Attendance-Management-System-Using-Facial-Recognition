from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import *
from .model_form import *
from .utility import *
import os

# Create your views here.

#Function for registering
def person_image_view(request):

	if request.method == 'POST':
			form = ImageForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('success')
	else:
		form = Image()
	return render(request, 'index.html', {'form' : form})

#Function for sucessful reegistration
def success(request):
	return HttpResponse('successfully uploaded')


#Function for markign attendance
def MarkAttendance(request):	
	if request.method == 'POST':
			form = AttendanceForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()

				ImgPath=""
				dir = 'media/unknown'
				for f in os.listdir(dir):
				   ImgPath=f"{dir}/{f}"

				
				name=Recognize(ImgPath)
				
				if len(name)!=0:
				  listToStr = ','.join([str(elem) for elem in name])  		
				else:
				  listToStr="All absent"

				for f in os.listdir(dir):
					os.remove(os.path.join(dir, f))
			
				return redirect(f'/present/{listToStr}/')
				
	else:
		form = AttendanceForm()
	return render(request, 'index.html', {'form' : form})


def present(request,name):
	return HttpResponse(f'{name}')
