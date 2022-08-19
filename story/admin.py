from django.contrib import admin
from  .models import Story,Category
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Story,SomeModelAdmin)
admin.site.register(Category)
