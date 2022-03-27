from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# models.py
class Image(models.Model):
	name = models.CharField(max_length=50)
	person_Img = models.ImageField(upload_to='images/')

class AttendanceImage(models.Model):
	Img = models.ImageField(upload_to='unknown/')

class Attendance(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	time=models.DateTimeField()