# Generated by Django 3.2.13 on 2022-05-16 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_title_post_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='exerpt',
        ),
    ]
