from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import BlogPost, BlogTag, BlogCategory, NewsLetter
from django.utils import timezone
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from blog.jalali_date_conv import shamsiDate
# Create your views here.


def index(request):
    posts = BlogPost.objects.all().order_by('-post_date')
    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/index.html', {
        'posts': posts,
        'tags': tags,
        'cats': cats,
        })


def post_single(request, slg):
    post = get_object_or_404(BlogPost, post_slug=slg)
    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/post.html', {
        'post': post,
        'tags': tags,
        'cats': cats,
        })


def tags(request):
    tags = BlogTag.objects.all().order_by('slug')
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/tags.html', {
        'tags': tags,
        'cats': cats,
        })


def tag_single(request, slg):
    tag = get_object_or_404(BlogTag, slug=slg)
    posts = tag.blogpost_set.all().order_by('-post_date')
    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/tag_single.html', {
        'tag': tag,
        'posts': posts,
        'tags': tags,
        'cats': cats,
        })


def categories(request):
    categories = BlogCategory.objects.all().order_by('slug')
    tags = BlogTag.objects.all()
    return render(request, 'blog/categories.html', {
        'categories': categories,
        'tags': tags,
        'cats': categories,
    })


def cat_single(request, slg):
    cat = get_object_or_404(BlogCategory, slug=slg)
    posts = cat.blogpost_set.all().order_by('-post_date')
    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/cat_single.html', {
        'cat': cat,
        'posts': posts,
        'tags': tags,
        'cats': cats,
        })


def newsletter(request):
        nl = NewsLetter()
        try:
            nl.email = request.POST['newsletter']
            nl.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
