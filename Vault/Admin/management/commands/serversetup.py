import datetime

from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        
        # Default groups within the platform
        groups = [
            "Administrators",
            "Human Resources",
            "Unassigned"
        ]

        admin_user_username = "Administrator"
        admin_user_password = "AdminPassword"


        # Build Default groups
        for g in groups:
            print(f'Creating Group {g}')
            ng = Group()
            ng.name = g
            ng.save()
        
        # Build Admin User
        admin_user = User()
        admin_user.username = admin_user_username
        admin_user.set_password(admin_user_password)
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.save()