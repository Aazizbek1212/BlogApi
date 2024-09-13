from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    
    
