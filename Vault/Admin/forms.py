from django import forms

from Admin.models import Share

class ShareForm(forms.ModelForm):
    
    class Meta:
        model = Share
        fields = ("server_name","directory")

