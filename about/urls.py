from django.conf.urls import url
from . import views
from django.urls import include, path
from.views import  aboutList,gallery_List,Privacy_List



app_name = 'about'

urlpatterns  = [

    path('', aboutList.as_view(),name='aboutList'),

    path('gallery_List' , views.gallery_List , name='gallery_List'),
    path('Privacy_List' , views.Privacy_List , name='Privacy_List'),




]
