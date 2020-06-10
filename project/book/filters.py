import django_filters
# from django_filters import DateFilter, CharFilter

from .models import Book

class BookFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Book
		fields = ('author','title','state')
		# exclude = ['customer', 'date_created']