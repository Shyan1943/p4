from django import forms
from dgs.models import IMDGCode


# SearchForm inherits from `forms.Form`, not `forms.ModelForm`
# This is because the search form doesn't have any models
# meaning it does not refer to any tables in our SQL database
class SearchForm(forms.Form):

    # the requried is `False` so that if the user leaves it blank
    # it will return all the information
    title = forms.CharField(max_length=100, required=False,
                            label="Title",
                            widget=forms.TextInput(
                                attrs={'placeholder': "Any keywords"}))

    # IMDGCode.objects.all() is eqv to "SELECT * FROM IMDGCode"
    # take the results of IMDGCode.objects.all and populate the <select>
    imdg_code = forms.ModelChoiceField(queryset=IMDGCode.objects.all(),
                                       required=False)
