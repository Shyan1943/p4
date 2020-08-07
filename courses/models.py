from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(blank=False, max_length=100)
    who_should_attend = models.CharField(blank=False, max_length=255)
    course_outline = models.TextField(blank=False)
    course_objectives = models.TextField(blank=False)
    accreditation_and_examination = models.CharField(blank=False,
                                                     max_length=255)
    course_fees = models.DecimalField(max_digits=10,
                                      decimal_places=3, blank=False)
    course_date = models.DateField(blank=False)

    def __str__(self):
        return self.title
