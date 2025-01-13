from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title