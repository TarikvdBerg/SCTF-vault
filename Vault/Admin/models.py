import json
import uuid

from django.db import models


# Create your models here.
class NetworkShare(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    server_name = models.CharField(max_length=255)
    address = models.GenericIPAddressField()
    total_storage = models.BigIntegerField()
    used_storage = models.BigIntegerField()

    @property
    def storagePercentageUsed(self):        
        # Caclulate storage percentage used
        return 0;

class LogMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    message_format = models.TextField();
    metadata = models.TextField();

    timestamp = models.DateTimeField(auto_now=True)

    FILE_SHARED = "FS"
    FILE_CREATED = "FC"
    FILE_EDITED = "FE"
    FILE_DELETED = "FD"
    USER_CREATED = "UC"
    USER_EDITED = "UE"
    USER_DELETED = "UD"
    NETWORK_SHARE_ADDED = "NSA"
    NETWORK_SHARE_EDITED = "NSE"
    NETWORK_SHARE_REMOVED = "NSR"

    activity_choices = (
        (FILE_SHARED, 'File Shared'),
        (FILE_CREATED, "File Created"),
        (FILE_EDITED, "File Edited"),
        (FILE_DELETED, "File Deleted"),
        (USER_CREATED, "User Created"),
        (USER_EDITED, "User Edited"),
        (USER_DELETED, "User Deleted"),
        (NETWORK_SHARE_ADDED, "Network Share Added"),
        (NETWORK_SHARE_EDITED, "Network Share Edited"),
        (NETWORK_SHARE_REMOVED, "Network Share Removed"),
    )

    LVL_DEBUG = "DEBU"
    LVL_INFO = "INFO"
    LVL_WARN = "WARN"
    LVL_ERR = "ERR"

    lvl_choices = (
        (LVL_DEBUG, "Debug"),
        (LVL_INFO, "Info"),
        (LVL_WARN, "Warning"),
        (LVL_ERR, "Error")
    )


    activity_type = models.CharField(max_length=3, choices=activity_choices, default=FILE_CREATED)
    warning_level = models.CharField(max_length=4, choices=lvl_choices, default=LVL_DEBUG)

    def setMessage(self, message, metadata):
        self.message_format = message
        self.metadata = json.dumps(metadata)
    
    def getFormatedMessage(self):
        js = json.loads(self.metadata)
        return self.message_format.format(js)
