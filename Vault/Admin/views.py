from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class AdminOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/overview.html"

class DanglingOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/dangling_file_overview.html"

class NetworkShareOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/network_shares.html"

class AddNetworkShare(TemplateView, LoginRequiredMixin):
    template_name = "admin/add_network_share.html"

class EditNetworkShare(TemplateView, LoginRequiredMixin):
    template_name = "admin/edit_network_share_modal.html"

class DeleteNetworkShare(TemplateView, LoginRequiredMixin):
    template_name = "admin/delete_network_share_modal.html"

class LogMessageOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/log_message_overview.html"

class SpecificLogmessageOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/log_message_single.html"
