from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from face_identify.views import posts_home
from face_identify.views import posts_detail
from face_identify.views import posts_list
from face_identify.views import posts_update
from face_identify.views import posts_delete
from face_identify.views import posts_create

from face_identify import views


app_name = 'posts'

urlpatterns = [
    path('', posts_home,name='list'),
    path('create/', posts_create),
    path('<int:id>/', posts_detail, name= 'detail'), 
    path('<int:id>/edit', posts_update, name= 'update'),
    path('<int:id>/delete', posts_delete),
]

