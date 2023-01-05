from django.db import models

# Create your models here.

class DocFile(models.Model):
    file = models.FileField(upload_to='', null=True, blank=True)
    filepath = models.CharField(null=True,max_length=999)
    filename = models.CharField(null=True, max_length=256)
    
