from django.db import models
from django.utils import timezone
import datetime
from slugify import slugify
from django.urls import reverse

# Create your models here.


class BlogTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag_single', args=[self.slug])


class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:cat_single', args=[self.slug])


class BlogPost(models.Model):
    post_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post_title = models.CharField(max_length=250)
    post_slug = models.SlugField(max_length=250, unique=True)
    post_content = models.TextField()
    post_category = models.ManyToManyField(BlogCategory, blank=True)
    post_tag = models.ManyToManyField(BlogTag, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_created_date = models.DateTimeField(auto_now_add=timezone.now)
    post_last_modified_date = models.DateTimeField(auto_now=timezone.now)
    post_status = models.BooleanField(default=True, verbose_name='Publish?')

    class meta:
        ordering = ('-post_last_modified_date',)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.post_slug])


class NewsLetter(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)
    date = models.DateTimeField(auto_now=timezone.now())

    def __str__(self):
        return self.email
