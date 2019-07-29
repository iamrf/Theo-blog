# Generated by Django 2.2.3 on 2019-07-27 16:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=250)),
                ('post_slug', models.SlugField(default=models.CharField(max_length=250), max_length=250, unique=True)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2019, 7, 27, 16, 4, 13, 546966))),
                ('post_created_date', models.DateTimeField(auto_now_add=True)),
                ('post_last_modified_date', models.DateTimeField(auto_now=True)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_tag', models.ManyToManyField(blank=True, to='blog.BlogTag')),
            ],
        ),
    ]