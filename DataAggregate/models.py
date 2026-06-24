from django.db import models

from LoadingFile.models import LoadFile
from User.models import CustomUser


class AggregateData(models.Model):
    load_file = models.ForeignKey(LoadFile , on_delete=models.CASCADE)
    group_by_value = models.PositiveSmallIntegerField(null=True , blank=False)
    aggregate_value = models.FloatField(null=True , blank=False)
