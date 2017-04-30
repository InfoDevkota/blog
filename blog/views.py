from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import BlogPage

def home(request):
    template_name = 'index.html'
    context = {'title':'Home'}
    return render(request,template_name,context)

def page(request, slug):
    template_name = 'page.html'
    infor = get_object_or_404(BlogPage, slug=slug)
    context = {'title':infor.title, 'infor':infor}
    return render(request,template_name,context)
