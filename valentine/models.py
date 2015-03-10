from django.db import models
from django.utils import timezone
import datetime

class UserEntry(models.Model):
	match_email=models.EmailField(max_length=100,blank=True,null=True)
	user_fullname=models.CharField(max_length=100)
	user_email=models.EmailField(max_length=100,unique=True)
	user_pic = models.ImageField(blank = True, null = True)
	#user_altemail=models.EmailField(max_length=100,default=0000)
	date_of_selection=models.DateTimeField('date of selction',blank=True,null=True)
	date_of_match=models.DateTimeField('date of match',blank=True,null=True)
	#place=models.CharField(max_length=20,blank=True,null=True)
	ip_address=models.GenericIPAddressField()
	gender = models.CharField(max_length= 10) #False = Male
	friends_count=models.IntegerField(max_length=5,blank=True,null=True)
class EntryChoice(models.Model):
	choice = models.ForeignKey(UserEntry)
	choice_names=models.CharField(max_length=100)
	choice_email=models.EmailField(max_length=100)
	choice_altemail=models.EmailField(max_length=100)




