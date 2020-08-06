from django import forms
from dgs.models import Dg, IMDGCode


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    imdg_code = forms.ModelChoiceField(queryset=IMDGCode.objects.all(),
                                       required=False)
