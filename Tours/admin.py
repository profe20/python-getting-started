from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin

from .models import Tours,ToursImages,SpecialOffers,Hotels,Pricess,ToursBook,TripType,Destinations,Duration,GroupSize,category,ToursReview
from .models import Nationality,Comment,Important_links,featureTours
# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
class ToursAdmin(admin.ModelAdmin):


    search_fields = ['category', 'Destinations','SpecialOffers','GroupSize' ]
    list_filter = [ 'Destinations','SpecialOffers','category']
    list_display = ['user' , 'Destinations','category' ]

admin.site.register(Tours,ToursAdmin)
admin.site.register(ToursImages)
admin.site.register(SpecialOffers)
admin.site.register(Destinations)
admin.site.register(TripType)
admin.site.register(Duration)
admin.site.register(GroupSize)
admin.site.register(Hotels)
admin.site.register(category)
admin.site.register(ToursBook)
admin.site.register(Nationality)
admin.site.register(Important_links)
admin.site.register(featureTours)
