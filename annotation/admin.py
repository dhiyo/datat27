from django.contrib import admin

from django.contrib import admin
from annotation.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Image,ImageAdmin)

# Register your models here.


