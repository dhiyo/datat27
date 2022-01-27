from django.urls import path
app_name='annotation'

from . import views

urlpatterns = [
    path('tagger/', views.tagger, name='tagger'),
]