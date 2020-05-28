from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class MainView(TemplateView, LoginRequiredMixin):
    template_name = "file/file_overview.html"

class FileMetadataView(TemplateView, LoginRequiredMixin):
    template_name = "file/file_metadata_view.html"

class DownloadFileModalView(TemplateView, LoginRequiredMixin):
    template_name = "file/download_file_modal.html"

class UploadFileModalView(TemplateView, LoginRequiredMixin):
    template_name = "file/upload_file_modal.html"

class ShareFileModalView(TemplateView, LoginRequiredMixin):
    template_name = "file/share_file_modal.html"

class WhoSharedWithView(ListView, LoginRequiredMixin):
    model = User
    template_name = "file/who_shared_with_modal.html"