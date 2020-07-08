from django.contrib import admin
from UserManager.models import RegistrationConfirmation, UserMeta


@admin.register(RegistrationConfirmation)
class RegistrationConfirmationAdmin(admin.ModelAdmin):
    pass

@admin.register(UserMeta)
class UserMetaAdmin(admin.ModelAdmin):
    pass