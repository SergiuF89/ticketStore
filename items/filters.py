import django_filters
from items.models import Item, CategoryItem


class CategoryFilter(django_filters.FilterSet):
    genre = django_filters.ModelChoiceFilter(queryset=CategoryItem.objects.all())
    class Meta:
        model = Item
        fields = ['genre',]