from annotation.api.viewsets import ImageViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register('images',ImageViewSet)



