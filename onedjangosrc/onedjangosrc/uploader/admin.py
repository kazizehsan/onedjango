from django.contrib import admin

from .models import UploadedFile


class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'file_type', 'created_at', 'user')


admin.site.register(UploadedFile, UploadedFileAdmin)
