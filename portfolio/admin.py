from django.contrib import admin
from .models import Project

# this line shows the model 'Project' in the admin
admin.site.register(Project)
