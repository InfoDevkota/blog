from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User)
    date_published = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    category = models.ForeignKey(Category)

    content = models.TextField()


    def __str__(self):
        return self.title

class BlogPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
