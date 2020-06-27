import uuid

from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from Admin.models import Share, LogMessage


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
    name = models.CharField(max_length=1024)
    size = models.IntegerField()
    location = models.CharField(max_length=512, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    opened = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Folder(UploadsMetaData):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    parent_folder = models.ForeignKey('Folder', blank=True, null=True, on_delete=models.CASCADE)

    personal_vault_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="personal_user")
    department_vault = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    is_dangling_dump = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_dangling_dump:
            try:
                Folder.objects.get(is_dangling_dump=True)
                lm = LogMessage()
                lm.setMessage("A user tried to create a new dangling files folder, but one already existed. Trashed the new folder.", [])
                lm.save()
                return
            except Folder.DoesNotExist:
                pass
        super(Folder, self).save(*args, **kwargs)

class File(UploadsMetaData):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    document = models.FileField(upload_to='templates')
    created = models.DateTimeField(auto_now=True)
    opened = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now=True)
    parent_folder = models.ForeignKey('Folder', on_delete=models.CASCADE)
    
# Create Folder for New User
@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Folder(
            name=instance.username,
            size=0,
            owner=instance,
            parent_folder=None,
            personal_vault_user=instance
        ).save()

# Create Folder for New Group
@receiver(post_save, sender=Group)
def group_post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Folder(
            name=instance.name,
            size=0,
            parent_folder=None,
            department_vault=instance
        ).save()