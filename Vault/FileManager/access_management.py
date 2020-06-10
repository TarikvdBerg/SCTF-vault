from django.contrib.auth.models import User

from FileManager.models import AccessRights

def GrantAccess(target_user, access_right, object_id, content_object, content_type):
    """Provides designated permissions to user.
    Object ID can be either a file or folder."""

    GA = AccessRights(target_user=User,
                      access_right=ACCESS_RIGHT_CHOICES,
                      object_id=object_id,
                      content_object=content_object,
                      content_type=content_type)

    GA.save()