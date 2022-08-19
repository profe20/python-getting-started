from django.conf.urls import url
from . import views
from django.urls import include, path
from.views import Tourslist,ToursDetail

app_name = 'Tours'

urlpatterns  = [

    path('',views.Tourslist , name='Tourslist'),
    path( '<slug:slug>' ,ToursDetail. as_view(),name='Tours_detail'),







]
