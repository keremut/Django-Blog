from django.db import models
from ckeditor.fields import *
from django.utils.text import slugify

class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message=models.TextField(max_length=500)

class About(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    slug = models.SlugField(max_length=200,blank=True,editable=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Service,self).save(*args,**kwargs)
