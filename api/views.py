from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from annotation.models import Image
from .serializers import ImageSerializer

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer