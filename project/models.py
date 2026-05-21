from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
class Program(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='projects')
    program = models.ManyToManyField(Program, related_name='projects', blank=True)
    description = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
# class ProjectProgram(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)


    
# class Testimonial(models.Model):
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='testimonial')
#     message = models.TextField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.name
    
    
    