from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class galary(models.Model):
    pic_title=models.CharField(max_length=150)
    title_pic=models.ImageField(upload_to='galary_pic',)
    title_date=models.DateField(auto_now=False)
    
class help_desk(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=13)
    issue_type=models.CharField(max_length=150)
    issue_date=models.DateField( auto_now=False, auto_now_add=False)   
    issue_explain=models.TextField() 
    
    
    
    
class Story(models.Model):
    story_pic=models.ImageField(upload_to='story_pic',)
    story_title=models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    about_story=models.TextField()
    
    
    
    
    
    
class yatra(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE)
        name=models.CharField( max_length=150)
        surname=models.CharField( max_length=150)
        email=models.EmailField( max_length=254)
        dob=models.DateField(auto_now=False, auto_now_add=False)
        adres=models.CharField(max_length=612)
        mobile=models.CharField(max_length=12)
        edu=models.CharField(max_length=1210)
        texp=models.CharField(max_length=12)
        spk=models.CharField(max_length=1288)
        afil=models.FileField(upload_to=None, max_length=100)

    
    

    
    
    
    
