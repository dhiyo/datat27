

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('annotation/', include('annotation.urls'),name='annotation'), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),	
    path('act/', TemplateView.as_view(template_name='home.html'), name='template2'),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),	
]
