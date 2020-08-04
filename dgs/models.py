from django.db import models


# Create your models here.
class Dg(models.Model):
    title = models.CharField(blank=False, max_length=255)
    example = models.CharField(blank=False, max_length=500)
    prohibited_reason = models.CharField(blank=False, max_length=800)

    def __str__(self):
        return self.title
