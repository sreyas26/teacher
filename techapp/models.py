from django.db import models

# Create your models here.

class Teacher(models.Model):
    address = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    c_number = models.IntegerField()
    courses= models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/", null=True)