from django.db import models

# Create your models here.

from django.db import models
  
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def _str_(self):
    	return self.title
