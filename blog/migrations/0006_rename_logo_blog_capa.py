# Generated by Django 5.1.2 on 2024-11-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='logo',
            new_name='capa',
        ),
    ]