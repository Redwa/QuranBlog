# Generated by Django 4.1.5 on 2023-03-25 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_post_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='video',
            new_name='video_link',
        ),
    ]
