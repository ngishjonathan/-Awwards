from django.db import models

from django.db import models

import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator,MinValueValidator

from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User,null=True,related_name='profile')
    prof_pic = models.ImageField(upload_to = 'awards/',default='Profile Pic')
    bio = models.CharField(max_length=300)
    contact = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.contact 

    def save_profile(self):
        self.save()

    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_profile,sender=User)
        # user = request.user
        # profile = Profile.objects.filter(user=user).first()
        # return profile

class Project(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'ards/',default='Project Image')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls,title):
        project = cls.objects.filter(title__icontains=title)
        # Q(title__icontains=title) |
        # Q(profile__user__icontains=owner)
        # )
        return project


class Review(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    design = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    usability = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    content = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def save_review(self):
        self.save()        
