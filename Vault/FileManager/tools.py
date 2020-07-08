from Admin.models import Share
from FileManager.models import File


def GetDanglingFiles(share=None):
    """GetDanglingFiles Checks the disk against the database to find files
    that don't occur in the database and reports the filename and hash
    back to the caller.

    Args:
        share ([type], optional): Optional single share to check, providing None results in all shares being checked. Defaults to None.

    Returns:
        list: A list of dictionaries containing the id, hash and path of each file.
    """

    totalDanglingFiles = []

    if share == None:
        # If no share is passed, grab all shares
        for s in Share.objects.all():
            totalDanglingFiles +=_checkShareForFiles(s)
        
        return totalDanglingFiles

    else:
        assert isinstance(share, Share)
        return _checkShareForFiles(share)


def _checkShareForFiles(share : Share) -> list:
    """Checks a share for the reported files and matches them
    against what is stored in the database. Returns a list of
    files that couldn't be found in the database.

    Args:
        share (Share): The instance of Share to check

    Returns:
        list: A list of dictionaries containing the id, hash and path of each file.
    """    
    reportedFiles = share.reportFiles()
    danglingFiles = []
    for rf in reportedFiles:
        try:
            File.objects.get(id=rf["id"])
        except:
            danglingFiles.append(rf)
            pass


    return danglingFiles