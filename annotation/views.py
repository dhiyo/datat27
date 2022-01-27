from django.http import HttpResponse
from django.shortcuts import render

def tagger(request):
	return render(request, 'annotation/tagger.html')

def index(request):
	return render(request, 'mlapi/home.html')


from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageSerializer
from .models import Image

# Create your views here.

class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()