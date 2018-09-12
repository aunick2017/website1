from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from face_identify.views import posts_home
from face_identify.views import posts_detail
from face_identify.views import posts_list
from face_identify.views import posts_update
from face_identify.views import posts_delete
from face_identify.views import posts_create
from face_identify.views import posts_coupon1
from face_identify.views import posts_coupon2
from face_identify.views import posts_coupon3
from face_identify.views import posts_coupon4
from face_identify.views import coup1
from face_identify.views import coup2
from face_identify.views import coup3
from face_identify.views import coup4


app_name = 'posts'

urlpatterns = [
    path('', posts_home,name='list'),
    path('create/', posts_create, name='create'),
    path('<int:id>/', posts_detail, name= 'detail'), 
    path('<int:id>/edit', posts_update, name= 'update'),
    path('<int:id>/delete', posts_delete),
    path('detail_coupon1/', posts_coupon1, name='detail_coupon1'),
    path('detail_coupon2/', posts_coupon2, name='detail_coupon2'),
    path('detail_coupon3/', posts_coupon3, name='detail_coupon3'),
    path('detail_coupon4/', posts_coupon4, name='detail_coupon4'),
    path('coupon1/', coup1, name='coup1'),
    path('coupon2/', coup2, name='coup2'),
    path('coupon3/', coup3, name='coup3'),
    path('coupon4/', coup4, name='coup4'),
]

