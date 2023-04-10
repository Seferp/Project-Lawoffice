from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': "Podaj imię",
            'user_email': 'Podaj adres email',
            'text': 'Komentarz'
        }