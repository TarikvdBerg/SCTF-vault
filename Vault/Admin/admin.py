from django.contrib import admin

from Admin.models import Share, LogMessage

# Register your models here.
@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    pass

@admin.register(LogMessage)
class LogMessageAdmin(admin.ModelAdmin):
    pass