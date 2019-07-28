from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<slug:slg>', views.tag_single, name='tag_single'),
    path('tags/', views.tags, name='tags'),
    path('categories/<slug:slg>/', views.cat_single, name='cat_single'),
    path('categories/', views.categories, name='categories'),
    path('post/<slug:slg>/', views.post_single, name='post_single'),
]
