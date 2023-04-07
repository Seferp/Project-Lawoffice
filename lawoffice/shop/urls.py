from django.urls import path
from . import views

urlpatterns = [
    path('sklep', views.shop_home_page, name='shop'),
    path('umowy', views.Contracts.as_view(), name='contracts'),
    path('pozwy', views.Lawsuit.as_view(), name='lawsuits'),
    path('pisma', views.Writings.as_view(), name='writings'),

    path('umowy/<slug:slug>', views.ItemDetail.as_view(), name='contract-detail'),
    path('pozwy/<slug:slug>', views.ItemDetail.as_view(), name='lawsuits-detail'),
    path('pisma/<slug:slug>', views.ItemDetail.as_view(), name='writings-detail'),
]