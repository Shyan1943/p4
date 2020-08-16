from django import forms
from .models import Dg
from cloudinary.forms import CloudinaryJsFileField


class DgForm(forms.ModelForm):
    class Meta:
        model = Dg
        fields = ("topic", "example", "prohibited_reason",
                  "imdg_code", "image")
    image = CloudinaryJsFileField()
