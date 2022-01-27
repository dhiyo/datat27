from annotation.models import Image
from .serializers import ImageSerializer
from rest_framework import viewsets

class ImageViewSet(viewsets.ModelViewSet):
	queryset=Image.objects.all()
	serializer_class=ImageSerializer
