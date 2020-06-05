from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # orders the entries from the most recent and only take 5
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
