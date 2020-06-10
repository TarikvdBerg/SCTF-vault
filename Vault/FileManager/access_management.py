from django.contrib.auth.models import User

from FileManager.models import AccessRight

def GrantAccess(User):
    """Provides designated permissions to user.
    Object ID can be either a file or folder."""

    GA = AccessRight(target_user=User,
                      access_right=ACCESS_RIGHT_CHOICES,
                      object_id=object_id,
                      content_object=content_object,
                      content_type=content_type)

    GA.save()

