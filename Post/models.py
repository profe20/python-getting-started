from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.
#3   user-title-content-image-created
class Post (models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    tags = TaggableManager()
    title = models.CharField(max_length=50)
    content = RichTextField()
    category = models.ForeignKey('category', related_name='Post_category', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    image1 = models.ImageField(upload_to="main_product", blank=True, null=True)
    image2 = models.ImageField(upload_to="main_product" , blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)

    def __str__(self):
       return self.title

class category(models.Model):
    category = models.CharField(max_length=40)
    def __str__(self):
        return self.category