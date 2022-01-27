from rest_framework import routers
from django.urls import path,include
from rest_framework import routers

router = routers.SimpleRouter()

from . import views
router = routers.SimpleRouter()
router.register(r'Image', views.ImageViewSet)

urlpatterns = [
    path('', include('router.urls')),
] 