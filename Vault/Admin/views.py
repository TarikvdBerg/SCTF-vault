from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
class AdminOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/overview.html"

class ShareOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/shares.html"

class AddShare(TemplateView, LoginRequiredMixin):
    template_name = "admin/add_share.html"

class EditShare(TemplateView, LoginRequiredMixin):
    template_name = "admin/edit_share.html"

class DeleteShare(TemplateView, LoginRequiredMixin):
    template_name = "admin/delete_share.html"

class LogMessageOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/log_message_overview.html"

class SpecificLogmessageOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/log_message_single.html"