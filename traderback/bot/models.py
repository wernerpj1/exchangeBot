from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name