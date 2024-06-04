#from django.forms import ModelForm,Textarea
#from django.db import models
from django import forms


class UploadFileForm1(forms.Form):
    #title = forms.CharField(max_length=50)
    file1 = forms.FileField()
class UploadFileForm2(forms.Form):
    #title = forms.CharField(max_length=50)
    file2 = forms.FileField()
class Uploadsinglefile(forms.Form):
    #title = forms.CharField(max_length=50)
    single_file = forms.FileField()