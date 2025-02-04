from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):

    class is_active(models.TextChoices):
        DRAFT = 'DF', 'Nieopublikowany'
        Published = 'PB', 'Opublikowany'

    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField()
    content = models.TextField()
    is_active = models.CharField(max_length=2, choices=is_active.choices, default=is_active.DRAFT)
    tag = TaggableManager()


class Comment(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(auto_now=True, null=True)
