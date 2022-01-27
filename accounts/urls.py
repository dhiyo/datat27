# accounts/urls.py
from django.urls import path
from .import views

from .views import *

from .views import SignUpView
# app_name not appname
app_name= 'accounts'

urlpatterns = [
    path('', views.index),
    path('login/', views.logind, name='logind'),
    path('profile/', views.profile, name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
]