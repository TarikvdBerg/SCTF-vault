import hashlib
import json
import os
import shutil
import uuid

from django.db import models


# Create your models here.
class Share(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    server_name = models.CharField(max_length=255)
    directory = models.TextField()

    total_storage = models.BigIntegerField(default=0)
    used_storage = models.BigIntegerField(default=0)
    free_storage = models.BigIntegerField(default=0)

    @property
    def total_storage_gb(self):
        return int(self.total_storage / (1024**3) * 100) / 100

    @property
    def used_storage_gb(self):
        return int(self.used_storage / (1024**3) * 100) / 100

    @property
    def storagePercentageUsed(self):        
        # Caclulate storage percentage used
        return 0;

    def updateAvailableStorage(self):
        self.total_storage, self.used_storage, self.free_storage = shutil.disk_usage(self.directory)

    """
    ReportFiles builds a list of files that are contained within the share, it outputs a list of
    dictionaries containing both the ID and hash of the file in question. This can be used to
    review if any of the files have been lost but are still stored on disk
    """    
    def reportFiles(self):
        file_set = []
        
        for root, dirs, files in os.walk(self.directory):
            for name in files:
                if name == "control": continue

                with open(root+name, 'r') as f:
                    data = f.read()

                    fhash = hashlib.sha1(data.encode()).hexdigest()
                    print(fhash)
                    file_set.append(
                        {
                            "id": name,
                            "hash": fhash
                        }
                    )
        return file_set




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
        return self.message_format.format(*js)
