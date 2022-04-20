from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField




# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = CloudinaryField('image',blank=True)
    symptoms = models.TextField(max_length=200)
    prevention = models.TextField(max_length=200)
    location = models.CharField(max_length=100)
class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = CloudinaryField('image',blank=True)
    email = models.EmailField()
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE, null=True)


class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=200)
    # date = models.DateTime(auto_now=True)
    disease = models.ForeignKey(Disease,on_delete=models.CASCADE, null=True)
    
    
