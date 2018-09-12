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

import itertools
import operator

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

# Create your views here.

def posts_home(request):



	return render(request, "coupon1.html")

   	#return HttpResponse("<h1>Hello</h1>")



def coup1(request):

   	return HttpResponse("<h1>c1</h1>")

def coup2(request):

   	return HttpResponse("<h1>c2</h1>")

def coup3(request):

   	return HttpResponse("<h1>c3</h1>")

def coup4(request):

   	return HttpResponse("<h1>c4</h1>")

def coup5(request):

   	return HttpResponse("<h1>c4</h1>")

def coup6(request):

   	return HttpResponse("<h1>c4</h1>")

def coup7(request):

   	return HttpResponse("<h1>c4</h1>")

def coup8(request):

   	return HttpResponse("<h1>c4</h1>")

def coup9(request):

   	return HttpResponse("<h1>c4</h1>")

def coup10(request):

   	return HttpResponse("<h1>c4</h1>")



def reset(request):

	List.objects.all().delete()
	History.objects.all().delete()




def posts_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	#print("hello")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		#print(instance)
		#print(str(instance.timestamp)[:25] + ".jpg")
		#print(str(instance.timestamp).replace(" ", "_")[:25] + ".jpg")
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
		#History.objects.all().delete()
		if List.objects.first() is None:
			
			for encoding in unknown_face_encoding:
				i = 1
				unknown_face_encoding_lists.append(encoding.tolist())

				save = History(person_number = i, Location = instance.Location, Date = instance.Date )
				save.save()
				"hello1.1"

			


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
			print("length of known_faces_array:" + str(len(known_faces_array)))
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
						try:
							instance.history_display11 = str(History.objects.filter(person_number = str(first_match_index))[10].Date) + str(History.objects.filter(person_number = str(first_match_index))[10].Location)
						except:
							instance.history_display11 = ''
						try:
							instance.history_display12 = str(History.objects.filter(person_number = str(first_match_index))[11].Date) + str(History.objects.filter(person_number = str(first_match_index))[11].Location)
						except:
							instance.history_display12 = ''
						try:
							instance.history_display13 = str(History.objects.filter(person_number = str(first_match_index))[12].Date) + str(History.objects.filter(person_number = str(first_match_index))[12].Location)
						except:
							instance.history_display13 = ''
						try:
							instance.history_display14 = str(History.objects.filter(person_number = str(first_match_index))[13].Date) + str(History.objects.filter(person_number = str(first_match_index))[13].Location)
						except:
							instance.history_display14 = ''
						try:
							instance.history_display15 = str(History.objects.filter(person_number = str(first_match_index))[14].Date) + str(History.objects.filter(person_number = str(first_match_index))[14].Location)
						except:
							instance.history_display15 = ''
						try:
							instance.history_display16 = str(History.objects.filter(person_number = str(first_match_index))[15].Date) + str(History.objects.filter(person_number = str(first_match_index))[15].Location)
						except:
							instance.history_display16 = ''
						try:
							instance.history_display17 = str(History.objects.filter(person_number = str(first_match_index))[16].Date) + str(History.objects.filter(person_number = str(first_match_index))[16].Location)
						except:
							instance.history_display17 = ''
						try:
							instance.history_display18 = str(History.objects.filter(person_number = str(first_match_index))[17].Date) + str(History.objects.filter(person_number = str(first_match_index))[17].Location)
						except:
							instance.history_display18 = ''
						try:
							instance.history_display19 = str(History.objects.filter(person_number = str(first_match_index))[18].Date) + str(History.objects.filter(person_number = str(first_match_index))[18].Location)
						except:
							instance.history_display19 = ''
						try:
							instance.history_display20 = str(History.objects.filter(person_number = str(first_match_index))[19].Date) + str(History.objects.filter(person_number = str(first_match_index))[19].Location)
						except:
							instance.history_display20 = ''
						try:
							instance.history_display21 = str(History.objects.filter(person_number = str(first_match_index))[20].Date) + str(History.objects.filter(person_number = str(first_match_index))[20].Location)
						except:
							instance.history_display21 = ''
						try:
							instance.history_display22 = str(History.objects.filter(person_number = str(first_match_index))[21].Date) + str(History.objects.filter(person_number = str(first_match_index))[21].Location)
						except:
							instance.history_display22 = ''
						try:
							instance.history_display23 = str(History.objects.filter(person_number = str(first_match_index))[22].Date) + str(History.objects.filter(person_number = str(first_match_index))[22].Location)
						except:
							instance.history_display23 = ''
						try:
							instance.history_display24 = str(History.objects.filter(person_number = str(first_match_index))[23].Date) + str(History.objects.filter(person_number = str(first_match_index))[23].Location)
						except:
							instance.history_display24 = ''
						try:
							instance.history_display25 = str(History.objects.filter(person_number = str(first_match_index))[24].Date) + str(History.objects.filter(person_number = str(first_match_index))[24].Location)
						except:
							instance.history_display25 = ''
						try:
							instance.history_display26 = str(History.objects.filter(person_number = str(first_match_index))[25].Date) + str(History.objects.filter(person_number = str(first_match_index))[25].Location)
						except:
							instance.history_display26 = ''
						try:
							instance.history_display27 = str(History.objects.filter(person_number = str(first_match_index))[26].Date) + str(History.objects.filter(person_number = str(first_match_index))[26].Location)
						except:
							instance.history_display27 = ''
						try:
							instance.history_display28 = str(History.objects.filter(person_number = str(first_match_index))[27].Date) + str(History.objects.filter(person_number = str(first_match_index))[27].Location)
						except:
							instance.history_display28 = ''
						try:
							instance.history_display29 = str(History.objects.filter(person_number = str(first_match_index))[28].Date) + str(History.objects.filter(person_number = str(first_match_index))[28].Location)
						except:
							instance.history_display29 = ''
						try:
							instance.history_display30 = str(History.objects.filter(person_number = str(first_match_index))[29].Date) + str(History.objects.filter(person_number = str(first_match_index))[29].Location)
						except:
							instance.history_display30 = ''
						
						

						instance.identified_person = str(first_match_index)



						




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
		

			List.objects.all().delete()

			for encoding in known_faces_array:
				unknown_face_encoding_lists.append(encoding.tolist())
			#print(len(unknown_face_encoding_lists))
			unknown_face_encoding_strings = json.dumps(unknown_face_encoding_lists)
			known_face_encoding_stored = List(
				question_text = unknown_face_encoding_strings)
				#location = form.Location,
				#date = form.Date)
			known_face_encoding_stored.save()
			print(known_face_encoding_stored)


		#get list of known faces



		#if len()





		#print(unknown_face_encoding)

		#for i in len(unknown_face_encoding):
	#		unknown_face_encoding[i] = 

		#json.dumps(unknown_face_encoding.tolist())

		###

		last_4_locations = []

		for entry in History.objects.filter(person_number = instance.identified_person).order_by('-id')[:4]:
			last_4_locations.append(entry.Location)

		print(last_4_locations)


		if History.objects.filter(person_number = instance.identified_person).order_by('-id')[:5].count() == 5 and len(set(last_4_locations)) != 5 and last_4_locations.count('StarBucks') == 1 and last_4_locations[0] == "StarBucks":
			if most_common(last_4_locations) == 'Hugo Boss':

				context = {
					"form": form,
					"instance": instance,
				}



				return render(request, "post_coupon1.html", context)

		if History.objects.filter(person_number = instance.identified_person).order_by('-id')[:5].count() == 5 and len(set(last_4_locations)) != 5 and last_4_locations.count('StarBucks') == 1 and last_4_locations[0] == "StarBucks":
			if most_common(last_4_locations) == 'Zara':

				context = {
					"form": form,
					"instance": instance,
				}



				return render(request, "post_coupon2.html", context)

		if History.objects.filter(person_number = instance.identified_person).order_by('-id')[:5].count() == 5 and len(set(last_4_locations)) != 5 and last_4_locations.count('StarBucks') == 1 and last_4_locations[0] == "StarBucks":
			if most_common(last_4_locations) == 'Boost':

				context = {
					"form": form,
					"instance": instance,
				}



				return render(request, "post_coupon3.html", context)





		

			



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

def posts_coupon1(request,id=None):
	#instance = Post.objects.get(id=1 )
	instance = get_object_or_404(Post,id=id)
	context = {
		"title": "Detail",
		"instance": instance,
	}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request, "post_coupon1.html", context)

def posts_coupon2(request,id=None):
	#instance = Post.objects.get(id=1 )
	instance = get_object_or_404(Post,id=id)
	context = {
		"title": "Detail",
		"instance": instance,
	}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request, "post_coupon2.html", context)

def posts_coupon3(request,id=None):
	#instance = Post.objects.get(id=1 )
	instance = get_object_or_404(Post,id=id)
	context = {
		"title": "Detail",
		"instance": instance,
	}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request, "posts_coupon3.html", context)

def posts_coupon4(request,id=None):
	#instance = Post.objects.get(id=1 )
	instance = get_object_or_404(Post,id=id)
	context = {
		"title": "Detail",
		"instance": instance,
	}
	#return HttpResponse("<h1>Hello</h1>")
	return render(request, "posts_coupon4.html", context)

def posts_ticket(request,id=None):
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


