# Generated by Django 2.2.3 on 2019-07-27 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190727_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
