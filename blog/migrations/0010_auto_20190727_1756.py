# Generated by Django 2.2.3 on 2019-07-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpost_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_status',
            field=models.BooleanField(default=True, verbose_name='Publish now?'),
        ),
    ]
