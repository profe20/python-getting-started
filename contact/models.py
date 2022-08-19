from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    Phone  = models.CharField(max_length=22)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    instagram= models.URLField(max_length=254)
    facebook= models.URLField(max_length=254)
    twitter= models.URLField(max_length=254)
    WhatsApp= models.URLField(max_length=254)
    pinterest= models.URLField(max_length=254)
    viator= models.URLField(max_length=254)
    tripadvisor= models.URLField(max_length=254)
    logo= models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    logo2= models.ImageField(upload_to="main_product"  ,blank=True, null=True)

    def __str__(self):
       return self.place
