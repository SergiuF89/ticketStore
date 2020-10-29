from django.shortcuts import render
from django.views.generic import ListView
from items.models import Item

class HomeView(ListView):
    model = Item
    paginate_by = 4
    template_name = "home.html"
    context_object_name = 'items'


class CategoryRockView(ListView):
    model = Item
    template_name = 'rock_category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryRockView, self).get_context_data(**kwargs)
        context['rock_category'] = Item.objects.filter(genre=1)
        return context


class CategoryHouseView(ListView):
    model = Item
    template_name = 'house_category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryHouseView, self).get_context_data(**kwargs)
        context['house_category'] = Item.objects.filter(genre=2)
        return context

class CategoryHipHopView(ListView):
    model = Item
    template_name = 'hip_hop_category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryHipHopView, self).get_context_data(**kwargs)
        context['hip_hop_category'] = Item.objects.filter(genre=3)
        return context
