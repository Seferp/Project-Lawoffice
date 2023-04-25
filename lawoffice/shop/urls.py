from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopHomePage.as_view(), name='shop'),
    path('umowy/', views.Contracts.as_view(), name='contracts'),
    path('pozwy/', views.Lawsuit.as_view(), name='lawsuits'),
    path('pisma/', views.Writings.as_view(), name='writings'),

    path('umowy/<slug:slug>', views.ItemDetail.as_view(), name='contract-detail'),
    path('pozwy/<slug:slug>', views.ItemDetail.as_view(), name='lawsuit-detail'),
    path('pisma/<slug:slug>', views.ItemDetail.as_view(), name='writing-detail'),

    path('koszyk', views.cart_view, name='cart'),
    path('dodaj-do-koszyka/<slug:slug>', views.add_to_cart, name='add-to-cart'),
    path('usun-z-koszyka/<int:cart_id>', views.remove_from_cart, name='remove-from-cart'),
]