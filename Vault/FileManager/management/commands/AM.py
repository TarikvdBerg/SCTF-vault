from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from FileManager.models import AccessRights
from FileManager.access_management import GrantAccess

class Command(BaseCommand):

    def handle(self, **options):

        roy = User.objects.get(username="roy")
        CT = ContentType.objects.get(model="accessright")
        
        GrantAccess(target_user=roy, access_right="RO",
        object_id="2fb43a0f-b4ce-4fff-bf12-1aa9bd308cec",
        # content_object=content_object, 
        content_type=CT)