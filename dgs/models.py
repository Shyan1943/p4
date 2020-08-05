from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class IMDGCode(models.Model):
    IMO_class = models.IntegerField(blank=False)
    chemical_name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.chemical_name


class Dg(models.Model):
    title = models.CharField(blank=False, max_length=255)
    example = models.TextField(blank=False)
    prohibited_reason = models.TextField(blank=False)
    imdg_code = models.ForeignKey(IMDGCode,
                                  on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
