from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from Admin.models import *

# Create your views here.
class AdminOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servers"] = Share.objects.all()[:10]
        context["log_messages"] = LogMessage.objects.filter(warning_level__in=[LogMessage.LVL_WARN, LogMessage.LVL_ERR])[:30]
        return context
    

class DanglingOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/dangling_file_overview.html"

class ShareOverview(TemplateView, LoginRequiredMixin):
    template_name = "admin/network_shares.html"

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
