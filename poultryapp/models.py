from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    profile_photo = CloudinaryField('profile_photo', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Diseases(models.Model):
    name = models.CharField(max_length = 60)
    disease_image = CloudinaryField('disease_image', null=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='diseases', null=True)

    class Meta:
    
        ordering = ['pub_date']

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls, search_term):
        disease = cls.objects.filter(title__icontains=search_term)
        return disease
