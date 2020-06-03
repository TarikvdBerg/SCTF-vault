from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
import logging

from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from django.shortcuts import HttpResponse

from .forms import addUserForm
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

# Create your views here.
class LoginView(TemplateView):
    template_name = "user/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username == None or password == None:
            logger.debug("Authentication attempt with empty username/password")
            return HttpResponse("Wun is empty")
        
        logger.debug(f"Authentication attempt for {username}")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'user/login.html', {'login_form': AuthenticationForm(request.POST)})
        
        login(request, user)
        return redirect("/files/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_form"] = AuthenticationForm(request=self.request)
        return context

class RegisterView(TemplateView):
    template_name = "user/register.html"

class ViewUsersView(TemplateView, LoginRequiredMixin):
    model = User
    template_name = "user/list_view.html"

class ViewSingleUserView(TemplateView, LoginRequiredMixin):
    template_name = "user/single_user.html"

class AddSingleUserView(TemplateView, LoginRequiredMixin):
    template_name = "user/add_user.html"
    # def create_user(self, request):
    #     if request.method == 'POST':
    #         form = addUserForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             cd = form.changed_data
    #
    #         return HttpResponseRedirect('add')
    #
    #     else:
    #         form = addUserForm
    #     return render(request, 'user/add_user.html', context=form)

class EditSingleUserView(TemplateView, LoginRequiredMixin):
    template_name = "user/edit_user.html"

class InactivateUserView(UpdateView, LoginRequiredMixin):
    template_name = "user/inactivate_modal.html"

class DepartmentUserOverview(ListView, LoginRequiredMixin):
    model = Group
    template_name = "user/department_list_view.html"

