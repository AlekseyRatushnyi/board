# Generated by Django 4.2.1 on 2023-06-05 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0005_remove_post_h1_remove_post_tag_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
    ]
