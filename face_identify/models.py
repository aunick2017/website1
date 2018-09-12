

# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
import ast




Location_choice = (('Hugo Boss','Hugo Boss'), ('Zara','Zara'),('Boost','Boost'), ('StarBucks','StarBucks'))


def upload_location(instance, filename):
	name = str(instance.timestamp)[:25] + ".jpg"
	return name
# Create your models here.
class Post(models.Model):
	Location = models.CharField(choices = Location_choice, max_length=120)
	Date = models.DateField(null=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field",height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	print1 = models.CharField(max_length=120, default ='')
	print2 = models.CharField(max_length=120, default ='')
	print3 = models.CharField(max_length=120, default ='')
	print4 = models.CharField(max_length=120, default ='')
	print5 = models.CharField(max_length=120, default ='')
	id_of_people = models.CharField(max_length=120, default ='')
	history_display1 = models.CharField(max_length=120, default ='')
	history_display2 = models.CharField(max_length=120, default ='')
	history_display3 = models.CharField(max_length=120, default ='')
	history_display4 = models.CharField(max_length=120, default ='')
	history_display5 = models.CharField(max_length=120, default ='')
	history_display6 = models.CharField(max_length=120, default ='')
	history_display7 = models.CharField(max_length=120, default ='')
	history_display8 = models.CharField(max_length=120, default ='')
	history_display9 = models.CharField(max_length=120, default ='')
	history_display10 = models.CharField(max_length=120, default ='')
	history_display11 = models.CharField(max_length=120, default ='')
	history_display12 = models.CharField(max_length=120, default ='')
	history_display13 = models.CharField(max_length=120, default ='')
	history_display14 = models.CharField(max_length=120, default ='')
	history_display15 = models.CharField(max_length=120, default ='')
	history_display16 = models.CharField(max_length=120, default ='')
	history_display17 = models.CharField(max_length=120, default ='')
	history_display18 = models.CharField(max_length=120, default ='')
	history_display19 = models.CharField(max_length=120, default ='')
	history_display20 = models.CharField(max_length=120, default ='')
	history_display21 = models.CharField(max_length=120, default ='')
	history_display22 = models.CharField(max_length=120, default ='')
	history_display23 = models.CharField(max_length=120, default ='')
	history_display24 = models.CharField(max_length=120, default ='')
	history_display25 = models.CharField(max_length=120, default ='')
	history_display26 = models.CharField(max_length=120, default ='')
	history_display27 = models.CharField(max_length=120, default ='')
	history_display28 = models.CharField(max_length=120, default ='')
	history_display29 = models.CharField(max_length=120, default ='')
	history_display30 = models.CharField(max_length=120, default ='')
	show_print = models.CharField(max_length=120, default ='')
	identified_person = models.CharField(max_length=120, default ='')
	#Reset = models.BooleanField()


	def __str__(self):
		return self.Location
	
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
	
	def get_absolute_coupon1(self):
		return reverse("posts:detail", kwargs={"id": self.id})
	
	def get_absolute_coupon2(self):
		return reverse("posts:coupon2", kwargs={"id": self.id})

	def get_absolute_coupon3(self):
		return reverse("posts:coupon3", kwargs={"id": self.id})

	def get_absolute_coupon4(self):
		return reverse("posts:coupon4", kwargs={"id": self.id})

import json

class List(models.Model):
	question_text = models.TextField(max_length=20000)
	location = models.TextField(max_length=20000)
	date = models.DateTimeField(null=True)

	def __str__(self):
		return self.question_text

class History(models.Model):
	person_number = models.TextField(max_length=20000)
	Location = models.CharField(max_length=120)
	Date = models.DateField(null=True)


class History_display(models.Model):
	print1 = models.CharField(max_length=120, default ='')
	print2 = models.CharField(max_length=120, default ='')
	print3 = models.CharField(max_length=120, default ='')
	print4 = models.CharField(max_length=120, default ='')
	print5 = models.CharField(max_length=120, default ='')
	


"""
Classes
That store the information, when called on Foreign Key effectively makes them a list
"""
# class Appearances(models.Model):
# 	appearance = TextField(max_length=100)

# class Dates(models.Model):
# 	dates = DateTimeField(null=True) 


# class List_of_people(models.Model):
# 	# full_name = models.CharField(max_length=25)
#     # age = models.IntegerField()
#     # department = models.CharField(max_length=3)
#     # wage = models.FloatField()

# 	person = models.ForeignKey(List)
# 	appearances = models.ForeignKey(Appearances)
# 	dates = models.ForeignKey(Dates)