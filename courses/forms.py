from django import forms
from .models import Course, CourseDate


class CourseForm(forms.ModelForm):
    class Meta:
        models = Course
        fields = ("title", "who_should_attend", "course_outline", "course_objectives",
                  "accreditation_and_examination", "course_fees", "course_date")
