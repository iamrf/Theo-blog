from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import BlogPost, BlogTag, BlogCategory, NewsLetter, PostComment
from django.utils import timezone
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from blog.jalali_date_conv import shamsiDate
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    available_posts = BlogPost.objects.all().filter(post_fixed=False).order_by('-post_date')
    fixed_posts = BlogPost.objects.filter(post_fixed=True).order_by('-post_date')[:3]
    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')

    # Show 7 posts per page
    paginator = Paginator(available_posts, 7)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/index.html', {
        'posts': posts,
        'fixed_posts': fixed_posts,
        'tags': tags,
        'cats': cats,
    })


def post_single(request, slg):
    post = get_object_or_404(BlogPost, post_slug=slg)
    comments = PostComment.objects.filter(post__post_slug=slg).order_by('-date')
    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/post.html', {
        'post': post,
        'comments': comments,
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
    tag_posts = tag.blogpost_set.all().order_by('-post_date')
    # Show 10 tags per page
    paginator = Paginator(tag_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # aside tags and cats
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
    cat_posts = cat.blogpost_set.all().order_by('-post_date')
    # Show 10 cats per page
    paginator = Paginator(cat_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # aside tags and cats
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


def search(request):
    inp = request.POST['search']
    search = BlogPost.objects.filter(
        Q(post_content__icontains=inp) | Q(post_title__icontains=inp)
        ).order_by('-post_date')

    tags = BlogTag.objects.all()
    cats = BlogCategory.objects.all().order_by('slug')
    return render(request, 'blog/search_results.html', {
        'search': search,
        'inp': inp,
        'tags': tags,
        'cats': cats,
    })


def comment(request, slg):
    post = get_object_or_404(BlogPost, post_slug=slg)
    cmnt = PostComment()
    try:
        cmnt.post = post
        cmnt.name = request.POST['name']
        cmnt.email = request.POST['email']
        cmnt.content = request.POST['content']
    except:
        return HttpResponseRedirect(reverse('blog:post_single', args=[slg]))
    else:
        cmnt.save()
        return HttpResponseRedirect(reverse('blog:post_single', args=[slg]))