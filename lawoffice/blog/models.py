from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField()
    content = models.TextField()
    tag = models.ManyToManyField(Tag)


class Comment(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')