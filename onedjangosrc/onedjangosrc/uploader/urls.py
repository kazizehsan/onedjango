from django.urls import path
from . import views

app_name = 'uploader'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('download/<str:file_name>/', views.download, name='download'),
    path('', views.UploadedFileList.as_view(), name='list'),
]
