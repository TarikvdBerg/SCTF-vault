import shutil
import random

from Admin.models import Share
from FileManager.models import File


class ShareNotAccessibleException(Exception):
    pass

class DiskManager():
    share_list = None

    def __init__(self):
        self._reload_shares()

    def _reload_shares(self):
        self.share_list = Share.objects.all()

        for share in self.share_list:
            self.test_share_availability(share)
            self.update_share_storage(share)

    def test_share_availability(self, share):
        assert isinstance(share, Share)

        try:
            with open(share.directory + "control") as f:
                content = f.read()
                if content == "share okay":
                    pass
                else:
                    raise ShareNotAccessibleException;
        except FileNotFoundError:
            with open(share.directory + "control", "w") as f:
                f.write("share okay")

    def update_share_storage(self, share):
        share.total_storage, share.used_storage, share.free_storage = shutil.disk_usage(share.directory)
        share.save()

    # TODO: Force the random.choice to go over each and every share
    def _get_available_network_share(self, file_size):
        i = 0
        while True:
            if i > len(self.share_list): 
                return None
            
            i += 1
            share = random.choice(self.share_list)
            if share.free_storage > file_size:
                return share


    def upload_new_file(self, file, data):
        assert isinstance(file, File)

        share = self._get_available_network_share(len(data))

        with open(share.directory + str(file.id), 'w') as f:
            f.write(data)

        file.stored_on_share = share
        file.save()

    def upload_new_version_file(self, file, data):
        pass
    
    def get_file_data(self, file):
        assert isinstance(file, File)

        with open(file.stored_on_share.directory + str(file.id), 'r') as f:
            data = f.read()

        print(data)
        return data

    def index_shares(self):
        pass

    def _index_share(self, share):
        assert isinstance(share, Share)
