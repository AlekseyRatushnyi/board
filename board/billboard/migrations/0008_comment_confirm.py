# Generated by Django 4.2.1 on 2023-06-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
