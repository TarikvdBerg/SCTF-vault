from django import forms
from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class addUserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-controll','type':'text',
                                                                                                  'placeholder':'First Name'}))
    lastName = forms.CharField(label='Last Name', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-controll', 'type': 'text',
                                                              'placeholder': 'Last Name'}))
    roles = forms.ChoiceField(label='Role', choices=[('admin', 'Admin'), ('manager', 'Manager'), ('user', 'User'), ('hr', 'HR')])
    temp_password = forms.CharField(label='Temp password', max_length=100, widget=forms.TextInput(attrs={
        'class':'form-controll', 'type': 'text', 'placeholder': 'Temp Password'}))
    email = forms.EmailField(label='email', max_length=100, widget=forms.EmailInput(
        attrs={'class':'form-controll','type':'email', 'placeholder':'johndoe@contoso.com'}))

    def __init__(self, *args, **kwargs):
        super(addUserForm, self).__init__(*args, **kwargs)
        self.fields['groups'] = forms.ChoiceField(choices = [ (g.id, g.name) for g in Group.objects.filter() ])





class editUserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-controll','type':'text',
                                                                                                  'placeholder':'First Name'}))
    lastName = forms.CharField(label='Last Name', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-controll', 'type': 'text',
                                                              'placeholder': 'Last Name'}))
    department = forms.ChoiceField(label='department', choices=[('finance', 'Finance'), ('hr', 'HR'), ('it', 'IT')])
    roles = forms.ChoiceField(label='Role', choices=[('admin', 'Admin'), ('manager', 'Manager'), ('user', 'User')])
    new_passowrd = forms.CharField(label='Temp password', max_length=100, widget=forms.TextInput(attrs={
        'class':'form-controll', 'type': 'text', 'placeholder': 'Temp Password'}))
    repeat_passowrd = forms.CharField(label='Temp password', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-controll', 'type': 'text', 'placeholder': 'Temp Password'}))
    email = forms.EmailField(label='email', max_length=100, widget=forms.EmailInput(
        attrs={'class':'form-controll','type':'email', 'placeholder':'johndoe@contoso.com'}))
