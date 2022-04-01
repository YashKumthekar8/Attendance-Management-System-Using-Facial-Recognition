from django.db import models
from django.contrib.auth.models import User
import datetime


class Image(models.Model):
	name = models.ForeignKey(User,on_delete=models.CASCADE)
	person_Img = models.ImageField(upload_to='images/')

class AttendanceImage(models.Model):
	time=models.TimeField()
	date = models.DateField(default=datetime.date.today)
	Img = models.ImageField(upload_to='unknown/')

class Attendance(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	time=models.TimeField()