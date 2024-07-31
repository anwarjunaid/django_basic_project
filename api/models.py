from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    addedDate = models.DateTimeField(auto_now=True)