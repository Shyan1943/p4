from django import forms
from .models import Program


class CourseForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ("title", "date", "who_should_attend", "outline",
                  "objectives", "accreditation_and_examination", "fees")
