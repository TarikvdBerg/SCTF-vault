from Admin.models import Share
from FileManager.tools import GetDanglingFiles
from FileManager.models import Folder, File

def UpdateShareStorage():

    for s in Share.objects.all():
        s.updateAvailableStorage()

        print(f"Updated storage for {s.server_name}")

        s.save()

def UpdateDanglingFiles():
    dfFolder = Folder.objects.get(is_dangling_dump=True) 

    danglingFiles = GetDanglingFiles()

    for f in danglingFiles:
        newFile = File()
        newFile.id = f["id"]
        newFile.size = 0
        newFile.location = f["path"]
        newFile.parent_folder = dfFolder
        newFile.save()