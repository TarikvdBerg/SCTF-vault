from django.contrib import admin
from FileManager.models import AccessRight, Folder, File
# Register your models here.

@admin.register(AccessRight)
class AccessRightAdmin(admin.ModelAdmin):
    pass

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
