from django.urls import path
from FileManager.views import *

urlpatterns = [
    path('', MainView.as_view()),
    path('metadata/{file_id}/', FileMetadataView.as_view()),
    path('download/{file_id}/', DownloadFileModalView.as_view()),
    path('upload/{file_id}/', UploadFileModalView.as_view()),
    path('share/{file_id}/', ShareFileModalView.as_view()),
    path('shared_with/{file_id}', WhoSharedWithView.as_view())    
]
