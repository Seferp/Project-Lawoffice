from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.

def shop_home_page(request):
    return render(request, 'shop/shop-main-page.html')

class Contracts(ListView):
    model = Item
    template_name = 'shop/contracts-view.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        return Item.objects.filter(type__type='Umowa')


class Lawsuit(ListView):
    model = Item
    template_name = 'shop/lawsuits-view.html'
    context_object_name = 'lawsuits'

    def get_queryset(self):
        return Item.objects.filter(type__type='Pozew')


class Writings(ListView):
    model = Item
    template_name = 'shop/writings-view.html'
    context_object_name = 'writings'

    def get_queryset(self):
        return Item.objects.filter(type__type='Pismo')


class ItemDetail(DetailView):
    model = Item
    template_name = 'shop/item-detail.html'

