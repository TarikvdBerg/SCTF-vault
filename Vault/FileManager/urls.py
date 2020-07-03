from django.urls import path
from django.conf.urls.static import static
from django_downloadview import ObjectDownloadView

from FileManager.views import *
from FileManager.models import File
from Vault import settings

urlpatterns = [
    path('dangling/', DanglingFilesView.as_view()),
    path('department/<department>/', MainView.as_view()),
    path('metadata/{file_id}/', FileMetadataView.as_view()),
    path('download/<file_id>/', DownloadFileModalView.as_view()),
    path('upload/', UploadFileModalView.as_view()),
    path('share/{file_id}', ShareFileModalView.as_view()),
    path('shared_with/{file_id}', WhoSharedWithView.as_view()),
    path('upload_file/', UploadFileModalView.as_view()),
    path('file_info/', FileMetadataView.as_view()),
    path('file_browser/get_folder_content/', GetFolderContents),
    path('f/<folder>/', MainView.as_view()),
    path('folder/', FolderModelView.as_view()),
    path('folder/<folder_id>/', DeleteFolderView),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
