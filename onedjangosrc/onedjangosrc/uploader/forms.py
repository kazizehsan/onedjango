from django import forms
from .models import UploadedFile
from django.utils.translation import gettext_lazy as _


class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = [
            'file_type',
            'file'
        ]
        labels = {
            'file': _('Choose file...'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file_type'].widget.attrs.update({'class': 'custom-select'})
