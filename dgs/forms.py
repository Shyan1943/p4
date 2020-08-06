from django import forms
from .models import Dg, IMDGCode


class DgForm(forms.ModelForm):
    class Meta:
        model = Dg
        fields = ("title", "example", "prohibited_reason", "imdg_code")
