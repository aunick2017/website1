

# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
import ast

def upload_location(instance, filename):
	name = str(instance.timestamp)[:25] + ".jpg"
	return name
# Create your models here.
class Post(models.Model):
	Location = models.CharField(max_length=120)
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


	def __str__(self):
		return self.Location
	
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})

import json

class List(models.Model):
	question_text = models.TextField(max_length=200)
	location = models.TextField(max_length=200)
	date = models.DateTimeField(null=True)

	def __str__(self):
		return self.question_text

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