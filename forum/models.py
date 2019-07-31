from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Car(models.Model):
    brand = models.CharField(max_length=120)
    color = models.CharField(max_length=120)

    def __str__(self):
        return self.brand


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    posts = models.ManyToManyField(Post)
    car = models.ForeignKey(Car, related_name='authors', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
