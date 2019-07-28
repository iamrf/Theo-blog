from django.contrib import admin
from . import models
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_author', 'post_date']

admin.site.register(models.BlogPost, PostAdmin)
admin.site.register(models.BlogCategory)
admin.site.register(models.BlogTag)
