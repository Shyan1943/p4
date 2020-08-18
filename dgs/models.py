from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class IMDGCode(models.Model):
    IMO_class = models.IntegerField(blank=False)
    chemical_name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.chemical_name


class Dg(models.Model):
    topic = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    imdg_code = models.ForeignKey(IMDGCode,
                                  on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = CloudinaryField()

    def __str__(self):
        return self.topic
