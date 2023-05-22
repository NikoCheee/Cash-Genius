from django.db import models
from django.contrib.auth.models import User


def get_user():
    user = User.pk
    return user


class Category(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class EnglishArticle(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=250)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=get_user)
    english_version = models.OneToOneField(EnglishArticle, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
