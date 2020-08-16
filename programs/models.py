from django.db import models


# Create your models here.
class Program(models.Model):
    title = models.CharField(blank=False, max_length=100)
    date = models.DateField(blank=False)
    who_should_attend = models.CharField(blank=False, max_length=255)
    outline = models.TextField(blank=False)
    objectives = models.TextField(blank=False)
    accreditation_and_examination = models.CharField(blank=False,
                                                     max_length=255)
    fees = models.DecimalField(max_digits=10, decimal_places=3, blank=False)

    def __str__(self):
        return self.title
