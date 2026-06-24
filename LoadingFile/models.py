from django.db import models

from User.models import CustomUser


class LoadFile(models.Model):
    class LoadingFileStatus(models.TextChoices):
        Complete = 'complete',
        Error = 'error',
        Pending = 'pending'

    file_patch = models.FileField(upload_to='uploads/', blank=True, null=True)
    file_name = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=64)
    create_date = models.DateTimeField(auto_now_add=True)
    loading_status = models.CharField(
        max_length=10,
        choices=LoadingFileStatus.choices,
        default=LoadingFileStatus.Pending,
    )
    error = models.CharField(max_length=256 , blank=True , default='')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('file_hash', 'user')