from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from cloudinary.models import CloudinaryField
import datetime as dt
from PIL import Image
import cloudinary

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField(null=True)
    profile_photo= CloudinaryField('profile_photo',null=True)
    
  
    
    def __str__(self):
       return f'{self.user.username}Profile'  
class Project(models.Model):
    title = models.CharField(max_length=255)
    project_image = CloudinaryField('project_image',null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    description = models.TextField()
    link = models.CharField(max_length=255,null=True)
    porf_ref = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='projects',null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def no_of_ratings (self):
        ratings = Rating.objects.filter(project=self)
        return len(ratings)
    
    def average(self):
        sum = 0
        ratings=Rating.objects.filter(project = self)
        for rating in ratings:
            sum += ((rating.rate_design)+(rating.rate_usability)+(rating.rate_content))
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0
    @classmethod  
    def search_project(cls,search_item):
        projects = cls.objects.filter(title__icontains= search_item )
        return projects
    
    def __str__(self) :
        return self.title
RATE_CHOICES = [
    (1,'1 - awful2'),
    (2,'2 - Horrible'),
    (3,'3 - Terrible'),
    (4,'4 - Bad'),
    (5,'5 - OK'),
    (6,'6 - nice work'),
    (7,'7 - Good'),
    (8,'8 - Very Good'),
    (9,'9 - Perfect'),
    (10,'10 - Masterpiece')

]
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    review=models.TextField()
    rate_design = models.PositiveSmallIntegerField(choices=RATE_CHOICES,null=True)
    rate_usability = models.PositiveSmallIntegerField(choices=RATE_CHOICES,null=True)
    rate_content = models.PositiveSmallIntegerField(choices=RATE_CHOICES,null=True)
    
    def __str__(self):
        return self.user.username
        