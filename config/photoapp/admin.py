from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Photo, Comment

# Register my models here
admin.site.register(Photo)
admin.site.register(Comment)