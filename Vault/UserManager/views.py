from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.dispatch import receiver
from django.db.models.signals import post_save

from .forms import addUserForm
from UserManager.models import TemporaryPassword
from Vault.settings import EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_USE_TLS

import logging

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

class AccountInfoView(TemplateView):
    template_name = "user/user_account_overview.html"

class ViewUsersView(View):
    model = User
    template_name = "user/list_view.html"

    def get(self, request, *args, **kwargs):
        users = User.objects.values('username','is_active')
        return render(request, self.template_name, {'users': users})



class ViewSingleUserView(TemplateView, LoginRequiredMixin):
    template_name = "user/single_user.html"

class AddSingleUserView(View):
    model = User
    form_class = addUserForm
    initial = {'key': 'value'}
    template_name = "user/add_user.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['email'],
                                            email=cd['email'],
                                            password=cd['temp_password'],
                                            first_name=cd['firstName'],
                                            last_name=cd['lastName'])

            send_mail(subject="Your temporary password has arrived!",
                      from_email=EMAIL_HOST_USER,
                      recipient_list=[cd['email']],

                      message=render_to_string("temporary_password.txt", {
                        'user': cd['email'],
                        'temp_password': cd['temp_password'],
                        }),
                  
                      fail_silently=False,
                      auth_user=EMAIL_HOST_USER,
                      auth_password=EMAIL_HOST_PASSWORD)                                
            
            return HttpResponseRedirect('/users/add')
        return render(request, self.template_name, {'form': form})

class EditSingleUserView(TemplateView, LoginRequiredMixin):
    template_name = "user/edit_user.html"

class InactivateUserView(UpdateView, LoginRequiredMixin):
    template_name = "user/inactivate_modal.html"

class DepartmentUserOverview(ListView, LoginRequiredMixin):
    model = Group
    template_name = "user/department_list_view.html"

