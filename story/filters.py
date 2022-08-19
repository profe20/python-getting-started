import django_filters
from .models import Story

class storyFilter(django_filters.FilterSet):

    class Meta:
        model = Story
        fields = ['name', 'category', ]
