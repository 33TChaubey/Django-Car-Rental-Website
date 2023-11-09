import django_filters
from .models import Car


class CarsFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {'car_name': ['iexact', 'icontains'], 'company_name': ['iexact', 'icontains'],
                  'location': ['iexact'], 'const_per_hour': ['lte', 'gte'], 'cost_par_day': ['lte', 'gte']}
