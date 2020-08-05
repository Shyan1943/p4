from django.db import models
from dgs.models import Dg


# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    dg = models.ForeignKey(Dg, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.dg + " " + self.title
