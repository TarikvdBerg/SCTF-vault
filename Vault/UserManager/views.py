from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
import logging

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.
class LoginView(TemplateView):
    template_name = "user/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username == None or password == None:
            logger.debug("Authentication Attempt with empty username/password")
            return HttpResponse("Wun is empty")
        
        logger.debug(f"Authentication attempt for {username}")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return redirect("/users/login/")
        
        login(request, user)
        return redirect("/files/")

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

