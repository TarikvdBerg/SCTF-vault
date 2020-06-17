import uuid
from datetime import datetime

from django.contrib.auth.models import Group, User
from django.db import models


# Create your models here.
class RegistrationConfirmation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    verification_code = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()

    @property
    def is_valid(self):
        """
        Returns whether the registration token has already expired or not
        """
        if self.expiry_date < datetime.now():
            return True
        return False

class UserMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    manager_of_group = models.ForeignKey(Group, on_delete=models.PROTECT, blank=True, null=True)

    @property
    def is_manager(self):
        return self.manager_of_group != None

class TemporaryPassword(models.Model):
    """The ability to request and send a temporary password for the user."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temp_password = models.TextField()
