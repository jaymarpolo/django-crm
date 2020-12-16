import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    end_date = DateFilter(field_name='created', lookup_expr='lte')
    start_date = DateFilter(field_name='created', lookup_expr='gte')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'created']
