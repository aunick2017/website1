from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages

from .forms import PostForm
from .models import Post

# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2

##

from PIL import Image, ImageDraw
import face_recognition
import numpy as np
import pandas as pd
import os
from scipy import ndimage
from PIL import Image, ImageDraw
import face_recognition
from scipy import ndimage
import json

from .models import List
from .models import History

import datetime


# Create your views here.

def posts_home(request):

   	return HttpResponse("<h1>Hello</h1>")



def posts_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	#print("hello")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		print(instance)
		print(str(instance.timestamp)[:25] + ".jpg")
		print(str(instance.timestamp).replace(" ", "_")[:25] + ".jpg")
		image_name = str(instance.timestamp).replace(" ", "_")[:25].replace(":","") + ".jpg"

		image_path = os.path.join("C:/Users/LJC/media_cdn/", image_name)
		unknown_image = face_recognition.load_image_file(image_path)
		unknown_face_encoding = face_recognition.face_encodings(unknown_image)
		unknown_face_encoding_lists = []
		# faces = Faces(image_name)

		print1 = "So there's {} faces here \n".format(len(unknown_face_encoding))
		print(print1)
		instance.print1 = print1
		instance.save()
		print("hello1")
		
		people_in_this_photo = ''
		print(List.objects.first())
		#List.objects.all().delete()
		if List.objects.first() is None:
			
			for encoding in unknown_face_encoding:
				i = 1
				unknown_face_encoding_lists.append(encoding.tolist())

				save = History(person_number = i, Location = instance.Location, Date = instance.Date )
				save.save()

			


			unknown_face_encoding_strings = json.dumps(unknown_face_encoding_lists)
			known_face_encoding_stored = List(question_text = unknown_face_encoding_strings)
			known_face_encoding_stored.save()
		else:
			known_faces_str = List.objects.first().question_text
			known_faces_lists = json.loads(known_faces_str)
			known_faces_array =[]
			print("hello1.5")

			# known_face_array = np.array(known_faces_lists)
			for encoding in known_faces_lists:
				known_faces_array.append(np.array(encoding)) 
				#print("length of known_faces:" + str(len(known_faces_array)))

			for number,face in enumerate(unknown_face_encoding, start=1):
				#this is just the compare function, I should make it so we can toggle the distance threshold
				check_with_known_faces = face_recognition.compare_faces(known_faces_array, face) 
				face_distances = face_recognition.face_distance(known_faces_array, face)
				# faces.sameness()
				print2 = "there are {} matches for face {}, with the closest distance being {}".format(sum(face_distances < 0.45),number,min(face_distances))
				print(sum(face_distances < 0.45))
				print(print2)
				instance.print2 = print2
				print("hello2")

				if sum(face_distances < 0.45) > 0:
					first_match_index = list(face_distances).index(min(face_distances)) + 1
					print3 = "i have identified person {}, and i recognise them \n ".format(first_match_index)

					save = History(person_number = first_match_index, Location = instance.Location, Date = instance.Date )
					save.save()

					i = 1

					if i == 1:
						i = 90000
						try:
							instance.history_display1 = str(History.objects.filter(person_number = str(first_match_index))[0].Date) + str(History.objects.filter(person_number = str(first_match_index))[0].Location)
						except:
							instance.history_display1 = ''
						try:
							instance.history_display2 = str(History.objects.filter(person_number = str(first_match_index))[1].Date) + str(History.objects.filter(person_number = str(first_match_index))[1].Location)
						except:
							instance.history_display2 = ''
						try:
							instance.history_display3 = str(History.objects.filter(person_number = str(first_match_index))[2].Date) + str(History.objects.filter(person_number = str(first_match_index))[2].Location)
						except:
							instance.history_display3 = ''
						try:
							instance.history_display4 = str(History.objects.filter(person_number = str(first_match_index))[3].Date) + str(History.objects.filter(person_number = str(first_match_index))[3].Location)
						except:
							instance.history_display4 = ''
						try:
							instance.history_display5 = str(History.objects.filter(person_number = str(first_match_index))[4].Date) + str(History.objects.filter(person_number = str(first_match_index))[4].Location)
						except:
							instance.history_display5 = ''
						try:
							instance.history_display6 = str(History.objects.filter(person_number = str(first_match_index))[5].Date) + str(History.objects.filter(person_number = str(first_match_index))[5].Location)
						except:
							instance.history_display6 = ''
						try:
							instance.history_display7 = str(History.objects.filter(person_number = str(first_match_index))[6].Date) + str(History.objects.filter(person_number = str(first_match_index))[6].Location)
						except:
							instance.history_display7 = ''
						try:
							instance.history_display8 = str(History.objects.filter(person_number = str(first_match_index))[7].Date) + str(History.objects.filter(person_number = str(first_match_index))[7].Location)
						except:
							instance.history_display8 = ''
						try:
							instance.history_display9 = str(History.objects.filter(person_number = str(first_match_index))[8].Date) + str(History.objects.filter(person_number = str(first_match_index))[8].Location)
						except:
							instance.history_display9 = ''
						try:
							instance.history_display10 = str(History.objects.filter(person_number = str(first_match_index))[9].Date) + str(History.objects.filter(person_number = str(first_match_index))[9].Location)
						except:
							instance.history_display10 = ''
						




					instance.print3 = print3

					people_in_this_photo = people_in_this_photo + str(first_match_index) + ","

					print(print3)
					#people_in_this_photo.append(first_match_index)

				elif sum(face_distances < 0.45) == 0:
					known_faces_array.append(face)
					#database_dict[len(database_dict) + 1] = face
					print4 = "...added face {} to the database.".format(number)
					print5 = "i don't recognise this person, let's identify them as {} \n ".format(len(known_faces_array))
					
					save = History(person_number = len(known_faces_array), Location = instance.Location, Date = instance.Date )
					save.save()




					instance.print4 = print4
					instance.print5 = print5
					
					people_in_this_photo = people_in_this_photo + str(len(known_faces_array)) + ","
					print(print4 + '\n' + print5)

					#people_in_this_photo.append(len(database_dict))


				#people = List_of_people.objects.add(person=face, appearances=form.location, dates=form.Date)

			print(people_in_this_photo)
			people_in_this_photo = people_in_this_photo[:-1]
			instance.id_of_people = people_in_this_photo

			instance.save()
		

			#List.objects.all().delete()

			#for encoding in known_faces_array:
			#	unknown_face_encoding_lists.append(encoding.tolist())
			##print(len(unknown_face_encoding_lists))
			#unknown_face_encoding_strings = json.dumps(unknown_face_encoding_lists)
			#known_face_encoding_stored = List(
			#	question_text = unknown_face_encoding_strings,
			#	location = form.location,
			#	date = form.date)
			#known_face_encoding_stored.save()
			#print(known_face_encoding_stored)


		#get list of known faces



		#if len()





		#print(unknown_face_encoding)

		#for i in len(unknown_face_encoding):
	#		unknown_face_encoding[i] = 

		#json.dumps(unknown_face_encoding.tolist())

		###


		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
	#if request.method == "POST":
	#	print(request.POST.get("content"))
	#	print(request.POST.get("title"))
	context = {
		"form": form,
	}

	return render(request, "post_form.html", context)

#def posts_detail(request):
#	context = {
#	    "title": "List"
#	}
#    return render(request, "index.html", context)


def posts_detail(request,id=None):
	#instance = Post.objects.get(id=1 )
	instance = get_object_or_404(Post,id=id)
	context = {
		"title": "Detail",
		"instance": instance,
	}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request, "post_details.html", context)



def posts_list(request):
	queryset = face_identify.objects.all()
	context = {
		"object_list": queryset,
		"title": "List",

	}
	return render(request, "index.html", context)

def posts_update(request, id=None):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print(form.cleaned_data.get("title"))
		messages.success(request, "Saved", extra_tags='some-tag')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Saved")


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def posts_delete(request, id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("face_identify:list")


###############


