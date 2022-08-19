
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.text import slugify

# Create your models here.
class Tours(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    information=models.TextField()
    Itinerary=models.TextField()
    price=models.FloatField()
    discountprice=models.FloatField()
    net_price=models.FloatField(blank=True, null=True)
    price=models.FloatField()
    pricee=models.TextField(blank=True, null=True)
    category = models.ForeignKey('category', related_name='Tours_category', on_delete=models.CASCADE)
    Destinations = models.ForeignKey('Destinations', related_name='Destinations_place', on_delete=models.CASCADE)
    SpecialOffers = models.ForeignKey('SpecialOffers', related_name='SpecialOffers_place', on_delete=models.CASCADE)
    TripType = models.ForeignKey('TripType', related_name='TripType', on_delete=models.CASCADE)
    Duration = models.ForeignKey('Duration', related_name='Duration', on_delete=models.CASCADE)
    GroupSize = models.ForeignKey('GroupSize', related_name='Tours_GroupSize', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True,blank=True)
    new  = models.BooleanField(default=True)
    ended  = models.BooleanField(default=False)
    active  = models.BooleanField(default=True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
        super(Tours,self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.net_price= self.price-self.discountprice
        super(Tours,self).save(*args, **kwargs)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Tours:Tours_detail', kwargs={'slug': self.slug })


class ToursImages(models.Model):
   user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
   Tours = models.ForeignKey('Tours', related_name='Tours_Images', on_delete=models.CASCADE)
   image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
   created = models.DateTimeField(default=timezone.now)
   active  = models.BooleanField(default=True)

   def __str__(self):
       return str (self.Tours)

class SpecialOffers(models.Model):
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
  name = models.CharField(max_length=50)
  created = models.DateTimeField(default=timezone.now)
  active  = models.BooleanField(default=True)

  def __str__(self):
    return self.name

class Destinations(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class TripType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Duration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class GroupSize(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  created = models.DateTimeField(default=timezone.now)
  active  = models.BooleanField(default=True)

  def __str__(self):
     return self.name

class Hotels(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    Stars=models.IntegerField(default=0)
    image = models.ImageField(upload_to="main_product"  ,blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class category(models.Model):
    category = models.CharField(max_length=40)
    def __str__(self):
        return self.category

class Pricess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Tours = models.ForeignKey('Tours', related_name='Tours_Pricess', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    Prices = models.FloatField(max_length=40)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ToursReview(models.Model):

 user = models.ForeignKey(User, on_delete=models.CASCADE)
 Tours = models.ForeignKey('Tours', related_name='Tours_packages', on_delete=models.CASCADE)
 pricee=models.IntegerField(default=0)
 feedback=models.TextField(max_length=2000)
 created = models.DateTimeField(default=timezone.now)
 active  = models.BooleanField(default=True)

 def __str__(self):
    return str (self.packages)
count=(
(' 1 ', "1 "),
('2 ', "2"),
('3', "3"),
('4', "4"),
('5', "5"),
('6', "6"),
('7', "7"),
('8', "8"),
('9', "9"),
('10', "10"),
)
countt=(
(' 1 ', "1 "),
('2 ', "2"),
('3', "3"),
('4', "4"),
('5', "5"),
('6', "6"),
('7', "7"),
('8', "8"),
('9', "9"),
('10', "10"),
)
class ToursBook(models.Model):

 Tours = models.ForeignKey('Tours', related_name='Book_Tours', blank=True,  on_delete=models.CASCADE)
 name=models.CharField(max_length=60)
 Email= models.EmailField(max_length=260)
 Nationality = models.ForeignKey('Nationality', related_name='Nationality_Tours', on_delete=models.CASCADE)
 phone_number = models.CharField(max_length=12)
 adults=models.CharField(choices=count ,max_length=100)
 children=models.CharField(choices=countt ,max_length=100)
 From = models.DateTimeField(default=timezone.now)
 To = models.DateTimeField(default=timezone.now)
 created = models.DateTimeField(default=timezone.now)
 active  = models.BooleanField(default=True)


 def __str__(self):
     return str (self.name)




class Nationality (models.Model):
    Nationality  = models.CharField(max_length=60)
    created = models.DateTimeField(default=timezone.now)
    active  = models.BooleanField(default=True)
    def __str__(self):
        return self.Nationality


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    Tours = models.ForeignKey(Tours, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)


#

class Important_links(models.Model):

 user = models.ForeignKey(User, on_delete=models.CASCADE)
 CharitableGivin=models.TextField()
 TourandPrices=models.TextField()
 ChildrenPolicy=models.TextField()
 DepositandPayment=models.TextField()
 TourVoucher=models.TextField()
 CancellationPolicy=models.TextField()
 EmergencyCancellationPolicy=models.TextField()


def __str__(self):
    return self.CharitableGivin

class FeaturedPostManager(models.Manager):
    def featured_post(self):
        f_post = featureTours.objects.filter(is_draft=False).order_by('-date')[:1]
        return f_post


class featureTours(models.Model):

    Tours = models.OneToOneField(Tours, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    objects = FeaturedPostManager()


    def __str__(self):
        return str(self.Tours)
