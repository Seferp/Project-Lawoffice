from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'my_site/home.html')


def about_me_view(request):
    return render(request, 'my_site/about-me.html')

def contact_view(request):
    return render(request, 'my_site/contact.html')