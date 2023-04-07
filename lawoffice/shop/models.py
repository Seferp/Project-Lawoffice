from django.db import models

# Create your models here.


class Document(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Item(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    type = models.ForeignKey(Document, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
