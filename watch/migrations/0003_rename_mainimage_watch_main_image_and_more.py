# Generated by Django 4.2.7 on 2023-11-30 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_remove_watch_image_watch_is_mine_watch_mainimage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watch',
            old_name='mainImage',
            new_name='main_image',
        ),
        migrations.RenameField(
            model_name='watch',
            old_name='secondImage',
            new_name='second_image',
        ),
    ]
