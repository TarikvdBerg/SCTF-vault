from django.core.management.base import BaseCommand, CommandError

from FileManager.models import AccessRights
from FileManager.access_management import GrantAccess

class Command(BaseCommand):

    def handle(self, **options):

        GrantAccess(target_user=boogeyman, access_right=RO,
        object_id="2fb43a0f-b4ce-4fff-bf12-1aa9bd308cec",
        content_object=content_object, content_type=content_type)