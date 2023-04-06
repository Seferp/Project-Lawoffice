from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o-mnie', views.about_me_view, name='about_me'),
    path('kontakt', views.contact_view, name='contact'),
]