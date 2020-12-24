import django_filters
from Shop.models import *
from Checkout.models import *
from django_filters import CharFilter, RangeFilter


class productFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    start_price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    end_price = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['demand', 'brand', 'category', 'name']


class orderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'


class customerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = '__all__'
