# Generated by Django 3.0.6 on 2020-06-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileManager', '0007_auto_20200625_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='document',
            field=models.FileField(default=None, upload_to='templates'),
            preserve_default=False,
        ),
    ]
