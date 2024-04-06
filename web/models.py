from django.db import models
from accounts.models import User
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='catagorey',default='catagorey/pexels-christina-morillo-1181676.jpg',null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    image = models.ImageField(upload_to='course/',default='course/7.jpg',null=True,blank=True)
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to='video/',default='video/Saras_Day_-_featuring_the_Present_Simple.mkv')
    grammer = models.TextField(null=True,blank=True)
    about = models.TextField()
    date  = models.DateField(auto_now_add=True)
    catagorey = models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def Counter(self):
        c = Course.objects.filter(id=self.id).count()
        return c
        
    def __str__(self):
        return str(self.title)
    

class Customer(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True,related_name='registered_courses')
    pro = models.BooleanField(default=False)
    date  = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        # بررسی وجود جدول برای کاربر و کورس فعلی
        existing_table_count = Customer.objects.filter(user=self.user, Course=self.Course,pro=self.pro).count()
        if existing_table_count >= 1:
            return
        super().save(*args, **kwargs)


class Contact(models.Model):
    Name = models.CharField(max_length=26)
    Email = models.EmailField()
    Sunjects = models.CharField(max_length=50)
    Message = models.TextField()
    active  = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.Name

class About(models.Model):
    Title = models.CharField(max_length=70)
    bio   = models.TextField()
    logo  = models.ImageField(upload_to='logo/',default='logo/1.png')
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    date   = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Title
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    comment = models.CharField(max_length=40)
    date  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment



