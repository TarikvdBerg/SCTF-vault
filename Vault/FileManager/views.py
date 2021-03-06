import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict
from django.shortcuts import HttpResponse, render
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View)

from FileManager.models import Folder, File
from django.core import serializers

# Create your views here.
class MainView(TemplateView, LoginRequiredMixin):
    template_name = "file/file_overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            if kwargs['folder'] == "personal":
                f = Folder.objects.get(personal_vault_user=self.request.user)
                context['target_folder'] = f.id
        except KeyError:
            pass

        try:
            if kwargs['department'] != None:
                group = Group.objects.get(name=kwargs['department'])
                f = Folder.objects.get(department_vault=group.id)
                context['target_folder'] = f.id
        except KeyError:
            pass

        return context


class FileMetadataView(TemplateView, LoginRequiredMixin):
    template_name = "file/file_metadata_view.html"


class DownloadFileModalView(TemplateView, LoginRequiredMixin):
    template_name = "file/download_file_modal.html"

    def get(self, request, *args, **kwargs):

        if request.method == 'GET':

            FileID = self.kwargs['file_id']
            Object = File.objects.get(id=FileID)

            MyDownload = Object.document

            response = HttpResponse(MyDownload)
            response['Content-Disposition'] = 'attachment; filename=%s' % MyDownload

            return response

class UploadFileModalView(TemplateView, LoginRequiredMixin):
    template_name = "file/upload_file_modal.html"

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            UploadedFile = request.FILES['document']
            ParentFolderID = request.POST.get('folder_id')
            ParentFolder = Folder.objects.get(id=ParentFolderID)

            print(UploadedFile.name)
            print(UploadedFile.size)

            FS = FileSystemStorage()
            FS.save(name=UploadedFile.name,
                    content=UploadedFile)

            F = File(name=UploadedFile.name,
                     document=UploadedFile,
                     size=UploadedFile.size,
                     owner=self.request.user,
                     parent_folder=ParentFolder).save()

            return render(request, "file/file_overview.html")

class ShareFileModalView(TemplateView, LoginRequiredMixin):
    template_name = "file/share_file_modal.html"


class SharedFilesView(TemplateView, LoginRequiredMixin):
    template_name = "file/shared_files.html"


class WhoSharedWithView(ListView, LoginRequiredMixin):
    model = User
    template_name = "file/who_shared_with_modal.html"

class DanglingFilesView(TemplateView, LoginRequiredMixin):
    template_name = "file/dangling.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['target_folder'] = Folder.objects.get(is_dangling_dump=True).id

        return context


class FolderModelView(View):
    def post(self, *args, **kwargs):
        try:
            pf = Folder.objects.get(id=self.request.POST.get('parent_folder'))
            print(pf.id)
            f = Folder(
                name=self.request.POST.get('folder_name'),
                parent_folder=pf,
                size=0,
                owner=self.request.user
            ).save()
            return HttpResponse("Ok")
        except Exception as e:
            print(e)
            pass

def DeleteFolderView(request, folder_id):
        try:
            f = Folder.objects.get(id=folder_id)
            if f.is_root_folder:
                return HttpResponse("Can't delete root folders.")

            f.delete()
        except Folder.DoesNotExist:
            return HttpResponse("Already deleted.")
        except Exception as e:
            return HttpResponse(e)


        return HttpResponse("Folder deleted.")

def DeleteFileView(request, file_id):
        try:
            f = File.objects.get(id=file_id)

            f.delete()
        except File.DoesNotExist:
            return HttpResponse("Already deleted.")
        except Exception as e:
            return HttpResponse(e)


        return HttpResponse("Folder deleted.")

def GetFolderContents(request):
    # Retrieve folder id
    folder_id = request.GET.get('fid')
    folder = Folder.objects.get(id=folder_id)

    try:
        contained_folders = Folder.objects.filter(parent_folder=folder)
    except Folder.DoesNotExist:
        contained_folders = []

    try:
        contained_files = File.objects.filter(parent_folder=folder)
    except File.DoesNotExist:
        contained_files = []

    parent_folder = folder.parent_folder if folder.parent_folder != None else None

    # Builds the directory Path for the user interface in the form of
    # /directory/subdirectory/subsubdirectory/
    directories = []
    cf = folder
    while True:
        directories.append(cf.name)
        if cf.parent_folder == None:
            break;
        cf = cf.parent_folder

    path = "/".join(directories[::-1])

    contained_folders_json = json.loads(serializers.serialize('json', contained_folders))
    for i in contained_folders_json:
        owner = User.objects.get(id=i['fields']["owner"])
        i['fields']["owner"] = f"{owner.first_name} {owner.last_name}"

    contained_files_json = json.loads(serializers.serialize('json', contained_files))
    for i in contained_files_json:
        owner = User.objects.get(id=i['fields']["owner"])
        i['fields']["owner"] = f"{owner.first_name} {owner.last_name}"

    resp_dict = {
        "parent_folder": parent_folder if parent_folder == None else parent_folder.id,
        "contained_folders": contained_folders_json,
        "contained_files": contained_files_json,
        "path": path
    }

    return HttpResponse(json.dumps(resp_dict, cls=DjangoJSONEncoder))
