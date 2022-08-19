import django_filters
from .models import Tours

class ToursFilter(django_filters.FilterSet):

    class Meta:
        model = Tours
        fields =('category','Destinations','SpecialOffers','TripType','Duration','GroupSize')
