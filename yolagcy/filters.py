import django_filters

from taksist.models import TaxiProfile

class TaxiFilter(django_filters.FilterSet):
    class Meta:
        model = TaxiProfile
        fields = {'mobile':['icontains'], 'category':['exact'], 'status':['exact']}