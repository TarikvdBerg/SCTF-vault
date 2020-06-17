from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from FileManager.models import AccessRights

def GrantAccess(target_user, access_right, object_id,
                # content_object, 
                content_type):
    """Provides designated permissions to user.
    Object ID can be either a file or folder."""

    GA = AccessRights(target_user=target_user,
                      access_right=access_right,
                      object_id=object_id,
                      # content_object=content_object,
                      content_type=content_type)

    GA.save()
    print("Granted access.")
