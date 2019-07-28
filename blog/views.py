from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import BlogPost, BlogTag, BlogCategory
from django.utils import timezone
import datetime
from django.http import HttpResponse

# Create your views here.


def index(request):
    posts = BlogPost.objects.all().order_by('-post_date')
    tags = BlogTag.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts,
        'tags': tags,
        })


def post_single(request, slg):
    post = get_object_or_404(BlogPost, post_slug=slg)
    return render(request, 'blog/post.html', {'post': post})


def tags(request):
    tags = BlogTag.objects.all().order_by('slug')
    return render(request, 'blog/tags.html', {'tags': tags})


def tag_single(request, slg):
        tag = get_object_or_404(BlogTag, slug=slg)
        return render(request, 'blog/tag_single.html', {'tag': tag})


def categories(request):
        categories = BlogCategory.objects.all().order_by('slug')
        return render(request, 'blog/categories.html', {'categories': categories})


def cat_single(request, slg):
        cat = get_object_or_404(BlogCategory, slug=slg)
        return render(request, 'blog/cat_single.html', {'cat': cat})
