# Generated by Django 2.2.3 on 2019-07-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpost_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_status',
            field=models.BooleanField(default=True),
        ),
    ]
