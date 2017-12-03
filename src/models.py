from django.db import models

# Create your models here.
class animals(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    age = models.CharField(max_length=300)
    weight = models.CharField(max_length=300)
    url = models.CharField(max_length=300, default=None)