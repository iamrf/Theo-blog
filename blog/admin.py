from django.contrib import admin
from . import models
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_author', 'post_date']


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'date']


admin.site.register(models.BlogPost, PostAdmin)
admin.site.register(models.BlogCategory)
admin.site.register(models.BlogTag)
admin.site.register(models.NewsLetter, NewsLetterAdmin)
admin.site.register(models.PostComment, PostCommentAdmin)
