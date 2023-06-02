from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('o-mnie', views.about_me_view, name='about-me'),
    path('kontakt', views.contact_view, name='contact'),
    path('faq', views.FAQ.as_view(), name='faq'),
    path('specjalizacje', views.Specializations.as_view(), name='specialization'),
    path('specjalizacje/<slug:slug>', views.SpecializationsDetail.as_view(), name='specialization-detail'),
]