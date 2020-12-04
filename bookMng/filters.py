
import django_filters
from django_filters import NumberFilter
from django_filters import CharFilter
from .models import *
from django import forms

class BookFilter(django_filters.FilterSet):
    #custom fields that relate to an attribute in the model

    book_name = CharFilter(field_name="name", lookup_expr='icontains', label='Title')
    user = CharFilter(field_name="username__username", lookup_expr='icontains', label='Username')
    min_price_range = NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price_range = NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')

    class Meta:
        model = Book
        fields =['publishdate']
        exclude = ['picture', 'pic_path']