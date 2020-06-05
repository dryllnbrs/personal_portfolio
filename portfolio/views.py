from django.shortcuts import render
from .models import Project

def home(request):
    # grabs all items in the db
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

