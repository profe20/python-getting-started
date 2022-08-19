from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.rom django.contrib import admin
from .models import about ,gallery,Privacy

# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(gallery  )



admin.site.register(about ,SomeModelAdmin )
admin.site.register(Privacy  )
