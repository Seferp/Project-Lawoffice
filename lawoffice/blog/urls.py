from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHomePage.as_view(), name='blog'),
    path('<slug:slug>', views.SinglePost.as_view(), name='post-detail'),

]