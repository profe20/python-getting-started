from django.urls import path
from . import views


app_name='accounts'

urlpatterns = [
    path('user_login',views.user_login , name='user_login'),
    path('signup',views.signup , name='signup'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
]
