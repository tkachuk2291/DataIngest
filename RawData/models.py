from django.db import models

from LoadingFile.models import LoadFile


class RawData(models.Model):
    file = models.ForeignKey(LoadFile , on_delete=models.CASCADE)
    advertiser = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    start = models.DateField(null=True, blank=False)
    end = models.DateField(null=True, blank=False)
    format = models.CharField(max_length=256)
    platform = models.CharField(max_length=256)
    impr = models.BigIntegerField()

