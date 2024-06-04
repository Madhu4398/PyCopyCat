import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import django
django.setup()
import ast,_ast
from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from Compareit.forms import UploadFileForm1,Uploadsinglefile,UploadFileForm2
from Compareit.models import Result
from django.core.files.storage import default_storage,FileSystemStorage
from django.views.generic.edit import FormView
from django.core.files.base import ContentFile
from django.views.generic.base import TemplateView

 # Homepage page
def Home(request):
    return render(request,'Homepage.html')

 # Instructions page
def Instructions(request):
    return render(request,'instructions.html')

    # moredetails page
def read_file1(request):
    f = open('../../PyCopyCat/match1.txt', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "moredetails.html", context)

def read_file2(request):
    f = open('../../PyCopyCat/match2.txt', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "moredetails.html", context)

    #Uploading 1st file
def upload_file1(request):
    
    if request.method == 'POST':
        form = UploadFileForm1(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file1(request.FILES['file1'])
            return HttpResponseRedirect('file2')
            #return HttpResponseRedirect(reverse(index))
    else:
        form = UploadFileForm1()
        #print("el condition")
    return render(request, 'upload1.html', {'form': form})

    #Writing 1st file into file1
def handle_uploaded_file1(f1):
    with open('../../PyCopyCat/file1.py', 'wb+') as destination1:
        for chunk1 in f1.chunks():
            destination1.write(chunk1)
        destination1.close()


    #Uploading 2nd file
def upload_file2(request):
    if request.method == 'POST':
        form2 = UploadFileForm2(request.POST, request.FILES)
        if form2.is_valid():
            handle_uploaded_file2(request.FILES['file2'])
            return HttpResponseRedirect('result1')
    else:
        form2 = UploadFileForm2()
        print("fail")
    return render(request, 'upload2.html', {'form': form2})

    #Writing 2st file into file2
def handle_uploaded_file2(f2):
    with open('../../PyCopyCat/file2.py', 'wb+') as destination2:
        for chunk2 in f2.chunks():
            destination2.write(chunk2)
        destination2.close()

    #Uploading single file
def single_file(request):
    
    if request.method == 'POST':
        form = Uploadsinglefile(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file3(request.FILES['single_file'])
            return HttpResponseRedirect('upload2')
    else:
        form = Uploadsinglefile()
        #print("el condition")
    return render(request, 'upload1.html', {'form': form})

    #Writing single file into file1
def handle_uploaded_file3(f1):
    with open('../../PyCopyCat/file1.py', 'wb+') as destination:
        for chunk in f1.chunks():
            destination.write(chunk)
        destination.close()

    #Uploading folder files
def simple_upload(request):
    
    if request.method == 'POST' and request.FILES['files_folder']:
        file=request.FILES['files_folder']
        
        for afile in request.FILES.getlist('files_folder'):
            myfile = afile
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            
            #filename = settings.MEDIA_ROOT + "/" + myfile.name
            for chunk in file.chunks():
                myfile.write(chunk)
            myfile.close()
        return HttpResponseRedirect('result2')
    return render(request, 'upload.html')

    #Uploading folder files
def folder_upload(request):
    if request.method == 'POST' and request.FILES['folder_files']:
        file=request.FILES['folder_files']
        for afile in request.FILES.getlist('folder_files'):
            myfile = afile
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            #filename = settings.MEDIA_ROOT + "/" + myfile.name
            for chunk in file.chunks():
                myfile.write(chunk)
            myfile.close()
        
        return HttpResponseRedirect('result3')
    return render(request, 'folderupload.html')
