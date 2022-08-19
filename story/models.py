from django.db import models
from django.urls import  reverse
from django.utils.translation import gettext as _

# Create your models here.



class Category(models.Model):
    name=models.CharField(_("أعداد المجلة :"),max_length=150,db_index=True)
    slug=models.SlugField(unique=True)





    class Meta:
        ordering=('-name',)
        verbose_name_plural = "أعداد المجلة  "

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('story:story_by_category', args=[self.slug])

class Story(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(_("الاسم الكامل :"),max_length=200)
    title=models.CharField(_("اسم البحث :"),max_length=200)
    Authorpdf = models.FileField(upload_to ="main_tour")
    body=models.TextField(db_index=True)
    active  = models.BooleanField(default=True)
    publish=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=('-title',)
        verbose_name_plural = "مجلة"

    def __str__(self):
        return self.title
    def get_absolute_url(self):
       return reverse('story:story_detail',args=[self.id,])
