# Generated by Django 3.0.5 on 2020-05-28 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('size', models.IntegerField()),
                ('location', models.CharField(max_length=512)),
                ('created', models.DateTimeField(auto_now=True)),
                ('opened', models.DateTimeField()),
                ('edited', models.DateTimeField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('parent_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FileManager.Folder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('size', models.IntegerField()),
                ('location', models.CharField(max_length=512)),
                ('created', models.DateTimeField(auto_now=True)),
                ('opened', models.DateTimeField()),
                ('edited', models.DateTimeField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('parent_folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FileManager.Folder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessRights',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('access_right', models.CharField(choices=[('NA', 'No Access'), ('RO', 'Read Only'), ('WO', 'Write Only'), ('RW', 'Read and Write')], default='NA', max_length=2)),
                ('object_id', models.UUIDField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
