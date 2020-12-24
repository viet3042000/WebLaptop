import django_filters
from .models import *
from django_filters import CharFilter, RangeFilter


class productFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    start_price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    end_price = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['demand', 'brand', 'category', 'name']
