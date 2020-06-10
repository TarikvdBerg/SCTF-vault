from django.contrib import admin
from FileManager.models import AccessRights, Folder, File
# Register your models here.

@admin.register(AccessRights)
class AccessRightsAdmin(admin.ModelAdmin):
    pass

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
