# Generated by Django 3.1.7 on 2021-08-10 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210810_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumnail_path',
        ),
    ]