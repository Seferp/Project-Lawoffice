from django.db import models

# Create your models here.


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'{self.id}- {self.question}'

class Specialization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    excerpt = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
