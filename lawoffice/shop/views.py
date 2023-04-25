from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.decorators.csrf import csrf_exempt
from .models import Item, Cart, Document

# Create your views here.

class ShopHomePage(View):

    def get_contract(self):
        contract = Document.objects.filter(type='Umowa')
        return contract
    def get_writing(self):
        writing = Document.objects.filter(type='Pismo')
        return writing
    def get_lawsuit(self):
        lawsuit = Document.objects.filter(type='Pozew')
        return lawsuit


    def get(self, request):
        contract = self.get_contract()
        writing = self.get_writing()
        lawsuit = self.get_lawsuit()
        return render(request, 'shop/shop-main-page.html', {'contract': contract, 'writing': writing, 'lawsuit': lawsuit})




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



@csrf_exempt
def add_to_cart(request, slug):
    item = Item.objects.get(slug=slug)
    session_id = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_id=session_id, item=item)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('cart')

@csrf_exempt
def remove_from_cart(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('cart')

def cart_view(request):
    session_id = request.session.session_key
    cart_items = Cart.objects.filter(session_id=session_id)
    total_price = sum([cart_item.item.price * cart_item.quantity for cart_item in cart_items])
    if total_price == 0:
        total_price = ''
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'shop/cart.html', context)
