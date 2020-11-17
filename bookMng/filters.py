import django_filters
from django_filters import DateFilter
from django_filters import CharFilter
from .models import *

class BookFilter(django_filters.FilterSet):
    #custom fields that relate to an attribute in the model

    book_name = CharFilter(field_name="name", lookup_expr='icontains', label='Title')
    start_date = DateFilter(field_name="publishdate", lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name="publishdate", lookup_expr='lte', label='End Date')

    user = CharFilter(field_name="username__username", lookup_expr='icontains', label='Username')


    class Meta:
        model = Book
        fields =['price']
        exclude = ['picture', 'pic_path', 'publishdate']
