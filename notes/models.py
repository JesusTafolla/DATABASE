from django.db import models

# Create your models here.
class Notes(models.Model):
    user = models.TextField(blank=True)
    description = models.TextField(blank=True)
