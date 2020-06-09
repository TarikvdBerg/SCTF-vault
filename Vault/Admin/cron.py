from Admin.models import Share

def UpdateShareStorage():

    for s in Share.objects.all():
        s.updateAvailableStorage()

        print(f"Updated storage for {s.server_name}")

        s.save()
