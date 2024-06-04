from django.urls import re_path
from Compareit.views import upload_file1,upload_file2,simple_upload,single_file,folder_upload,Home
import Compareit.mainprog
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='homepage'),
    path('instructions',Compareit.views.Instructions,name='instructions'),
    path('file1/',Compareit.views.upload_file1,name='upload1'),
    path('file1/file2/',Compareit.views.upload_file2,name='file2'),
    path('file1/file2/result1/',Compareit.mainprog.percent,name='result1'),

    path('singlefile/',single_file,name='upload2'),
    path('singlefile/upload2/',Compareit.views.simple_upload,name='files_folder'),
    path('singlefile/upload2/result2/',Compareit.mainprog.percent2,name='result2'),

    path('folder_files/',Compareit.views.folder_upload,name='folder_files'),
    path('folder_files/result3/',Compareit.mainprog.percent3,name='result3'),
    
    path('result2/moredetails/',Compareit.views.read_file1,name='moredetails'),
    
    path('result3/moredetails2/',Compareit.views.read_file2,name='moredetails2'),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
