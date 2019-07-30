# Generated by Django 2.2.3 on 2019-07-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpost_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_status',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_category',
            field=models.ManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
    ]