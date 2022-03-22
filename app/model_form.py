# forms.py
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['name', 'person_Img']


class AttendanceForm(forms.ModelForm):
	class Meta:
		model = AttendanceImage
		fields = ['Img']
