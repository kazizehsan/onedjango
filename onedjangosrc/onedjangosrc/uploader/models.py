from django.db import models
from django.conf import settings

import calendar
import time

from .config import FILE_TYPES


def media_upload_path(instance, filename):
    return '{0}_{1}'.format(calendar.timegm(time.gmtime()), filename)


class UploadedFile(models.Model):
    file_type = models.CharField(max_length=255, choices=FILE_TYPES, default='a')
    file = models.FileField(upload_to=media_upload_path)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.file.name
