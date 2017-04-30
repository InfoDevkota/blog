from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogPage, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = {'slug':('title',)}

class BlogPageAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(Category, CategoryAdmin)
