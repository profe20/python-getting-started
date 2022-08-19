from django.db import models

# Create your models here.
class about (models.Model):

  Who_We_Are=models.TextField()
  Who_image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
  video= models.URLField(max_length=254)



  def __str__(self):
       return self.Who_We_Are


class  gallery (models.Model):

  gallery_Text=models.TextField(max_length=1000)
  gallery_image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)



  def __str__(self):
       return self.gallery_Text


class  Privacy (models.Model):

  Privacy_Text=models.TextField(max_length=1000)
  Privacy_Text2=models.TextField(max_length=1000)
