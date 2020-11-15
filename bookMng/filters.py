import django_filters
from django_filters import DateFilter
from django_filters import CharFilter
from .models import *

class BookFilter(django_filters.FilterSet):
    #custom fields that relate to an attribute in the model
    start_date = DateFilter(field_name ="publishdate", lookup_expr='gte')
    end_date = DateFilter(field_name="publishdate", lookup_expr='lte')
    class Meta:
        model = Book
        fields =['name', 'web', 'price', 'username__username']
        exclude = ['picture', 'pic_path', 'publishdate']

        #to change the name of the labels for the filters
        def __init__(self, *args, **kwargs):
            super(BookFilter, self).__init__(*args, **kwargs)
            self.filters['manufacturer'].extra.update(
                {'empty_label': 'All Manufacturers'})
