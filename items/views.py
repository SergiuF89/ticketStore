from django.shortcuts import render
from .filters import CategoryFilter
from .models import Item


def search(request):
    
    item_list = Item.objects.all()
    item_filter = CategoryFilter(request.GET, queryset=item_list)
    return render(request, 'shop/categories.html', {'filter': item_filter})
