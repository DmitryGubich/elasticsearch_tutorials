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
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
