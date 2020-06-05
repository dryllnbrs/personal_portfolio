from django.contrib import admin
from .models import Blog

# this line shows the model 'Blog' in the admin
admin.site.register(Blog)
