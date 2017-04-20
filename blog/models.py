from django.db import models

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
