import uuid

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Admin.models import Share


# Create your models here.
class AccessRights(models.Model):
    NO_ACCESS = 'NA'
    READ_ONLY = 'RO'
    WRITE_ONLY = 'WO'
    READ_WRITE = "RW"

    ACCESS_RIGHT_CHOICES = (
        (NO_ACCESS, 'No Access'),
        (READ_ONLY, 'Read Only'),
        (WRITE_ONLY, "Write Only"),
        (READ_WRITE, "Read and Write")
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    access_right = models.CharField(max_length=2, choices=ACCESS_RIGHT_CHOICES, default=NO_ACCESS)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField() # ID of the File or Folder
    # content_object = GenericForeignKey() # Type of object for the File or Folder

class UploadsMetaData(models.Model):
    size = models.IntegerField()
    location = models.CharField(max_length=512)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now=True)
    opened = models.DateTimeField()
    edited = models.DateTimeField()

    class Meta:
        abstract = True

class Folder(UploadsMetaData):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    parent_folder = models.ForeignKey('Folder', blank=True, null=True, on_delete=models.CASCADE)

class File(UploadsMetaData):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    
