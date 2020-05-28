from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group

# Create your views here.
class LoginView(TemplateView):
    template_name = "user/login.html"

class RegisterView(TemplateView):
    template_name = "user/register.html"

class ViewUsersView(ListView, LoginRequiredMixin):
    model = User
    template_name = "user/list_view.html"

class ViewSingleUserView(TemplateView, LoginRequiredMixin):
    template_name = "user/single_user.html"

class AddSingleUserView(CreateView, LoginRequiredMixin):
    template_name = "user/add_user.html"

class EditSingleUserView(UpdateView, LoginRequiredMixin):
    template_name = "user/edit_user.html"

class InactivateUserView(UpdateView, LoginRequiredMixin):
    template_name = "user/inactivate_modal.html"

class DepartmentUserOverview(ListView, LoginRequiredMixin):
    model = Group
    template_name = "user/department_list_view.html"

