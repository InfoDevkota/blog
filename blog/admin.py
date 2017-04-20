from django.contrib import admin

# Register your models here.
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(BlogPost,BlogPostAdmin)
