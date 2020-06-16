from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from FileManager.models import AccessRights

def GrantAccess(target_user, access_right, object_id,
                # content_object, 
                content_type):
    """Provides designated permissions to user.
    Object ID can be either a file or folder."""

    roy = User.objects.get(username="roy")
    CT = ContentType.objects.get(model="accessright")

    GA = AccessRights(target_user=roy,
                      access_right="RO",
                      object_id="2fb43a0f-b4ce-4fff-bf12-1aa9bd308cec",
                      # content_object=content_object,
                      content_type=CT)

    GA.save()
    print("Granted access.")
