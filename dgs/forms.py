from django import forms
from django.db.models import Q
from .models import Dg, IMDGCode


class DgForm(forms.ModelForm):
    class Meta:
        model = Dg
        fields = ("title", "example", "prohibited_reason", "imdg_code")


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    imdg_code = forms.ModelChoiceField(queryset=IMDGCode.objects.all(),
                                           required=False)
