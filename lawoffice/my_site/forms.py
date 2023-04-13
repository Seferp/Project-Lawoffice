from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label= 'Imię', max_length=100)
    last_name = forms.CharField(label= 'Nazwisko', max_length=100)
    email = forms.EmailField(label= 'Email')
    subject = forms.CharField(label= 'Temat', max_length=200)
    message = forms.CharField(label= 'Wiadomość', widget=forms.Textarea)
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']