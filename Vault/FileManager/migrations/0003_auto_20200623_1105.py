# Generated by Django 3.0.6 on 2020-06-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileManager', '0002_auto_20200609_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='stored_on_share',
        ),
    ]