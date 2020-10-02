import os
import mimetypes

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.conf import settings

from .forms import UploadedFileForm
from .models import UploadedFile


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('uploader:list'))
        return render(request, 'uploader.html', {"form": form})
    else:
        form = UploadedFileForm()
        return render(request, 'uploader.html', {"form": form})


@login_required
def download(request, file_name):
    if request.method == 'GET':
        file_path = settings.MEDIA_ROOT + '/' + file_name
        file_obj = open(file_path, 'rb')
        file_mimetype = mimetypes.guess_type(file_path)
        response = HttpResponse(file_obj, content_type=file_mimetype)
        response['Content-Length'] = os.stat(file_path).st_size
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        return response


@method_decorator(login_required, name='dispatch')
class UploadedFileList(ListView):
    paginate_by = 10
    context_object_name = 'file_list'
    queryset = UploadedFile.objects.order_by('-created_at')
    template_name = 'file_list.html'
