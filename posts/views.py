from django.shortcuts import render
from django.views.generic import ListView, DetailView
from items.models import Item
from users.models import UserProfile

from django.contrib.auth.models import User


class HomeView(ListView):
    model = UserProfile
    template_name = "home.html"
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['products'] = Item.objects.all()
        return context


class ProfileView(ListView):
    model = UserProfile
    template_name = 'navbar.html'
    context_object_name = 'users'


class CategoryAllView(ListView):
    model = Item
    template_name = 'all_categories.html'
    context_object_name = 'items'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryAllView, self).get_context_data(**kwargs)
        context['products'] = Item.objects.all()
        return context


class FooterListView(ListView):
    model = Item
    template_name = 'footer.html'
    context_object_name = 'products'




class CategoryRockView(ListView):
    model = Item
    template_name = 'rock_category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryRockView, self).get_context_data(**kwargs)
        context['rock_category'] = Item.objects.filter(genre=1)
        context['products'] = Item.objects.all()
        return context


class CategoryHouseView(ListView):
    model = Item
    template_name = 'house_category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryHouseView, self).get_context_data(**kwargs)
        context['house_category'] = Item.objects.filter(genre=2)
        context['products'] = Item.objects.all()
        return context

class CategoryHipHopView(ListView):
    model = Item
    template_name = 'hip_hop_category.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryHipHopView, self).get_context_data(**kwargs)
        context['hip_hop_category'] = Item.objects.filter(genre=3)
        context['products'] = Item.objects.all()
        return context
