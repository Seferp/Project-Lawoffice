from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from blog.models import Post
from shop.models import Document
from django.core.mail import send_mail

from .models import FAQ, Specialization
from .forms import ContactForm

# Create your views here.

class Home(View):
    def get_last_posts(self):
        posts = Post.objects.all().order_by('-date')
        return posts[:3]
    def get_specializations(self):
        specializations = Specialization.objects.all().order_by('id')
        return specializations
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
        posts = self.get_last_posts()
        specializations = self.get_specializations()
        contract = self.get_contract()
        writing = self.get_writing()
        lawsuit = self.get_lawsuit()
        return render(request, 'my_site/home.html', {'specializations': specializations, 'posts': posts, 'contract': contract, 'writing': writing, 'lawsuit': lawsuit})


def about_me_view(request):
    return render(request, 'my_site/about-me.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                'Kontakt z formularza',
                f'Imię: {first_name}\nNazwisko: {last_name}\nEmail: {email}\nTemat: {subject}\nWiadomość: {message}',
                email,
                ['p.seferyniak.test@gmail.com'],
                fail_silently=False,
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'my_site/contact.html', {'form': form})

class FAQ(ListView):
    model = FAQ
    template_name = 'my_site/faq.html'
    ordering = ['id']
    context_object_name = 'faqs'

class Specializations(ListView):
    model = Specialization
    template_name = 'my_site/specialization.html'
    ordering = ['id']
    context_object_name = 'specializations'

class SpecializationsDetail(DetailView):
    model = Specialization
    template_name = 'my_site/specialization-detail.html'



