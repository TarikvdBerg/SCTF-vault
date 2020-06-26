from django.urls import path
from FileManager.views import *

urlpatterns = [
    path('dangling/', DanglingFilesView.as_view()),
    path('department/<department>/', MainView.as_view()),
    path('metadata/{file_id}/', FileMetadataView.as_view()),
    path('download/{file_id}/', DownloadFileModalView.as_view()),
    path('upload/{file_id}/', UploadFileModalView.as_view()),
    path('share/{file_id}', ShareFileModalView.as_view()),
    path('shared_with/{file_id}', WhoSharedWithView.as_view()),
    path('upload_file/', UploadFileModalView.as_view()),
    path('file_info/', FileMetadataView.as_view()),
    path('file_browser/get_folder_content/', GetFolderContents),
    path('/f/<folder>/', MainView.as_view()),
]