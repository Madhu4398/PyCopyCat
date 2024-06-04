#mainprog file used for getting results page
import ast
from difflib import SequenceMatcher
import difflib
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import os
from Compareit.newfilesmatch import multi_files
from Compareit.folderfilescmp import folder_match

# Creating AST
def dumps():
    open('../../PyCopyCat/file1_dump.py', 'w').close()
    open('../../PyCopyCat/file2_dump.py', 'w').close()
    file1=ast.parse(open('../../PyCopyCat/file1.py').read())
    file2=ast.parse(open('../../PyCopyCat/file2.py').read())
    file1_dump=ast.dump(file1)
    with open('../../PyCopyCat/file1_dump.py','wt')as f1:
        f1.write(file1_dump)
    file2_dump = ast.dump(file2)
    with open('../../PyCopyCat/file2_dump.py','wt')as f2:
        f2.write(file2_dump)


# File-File comparison
def percent(request):
   
    dumps()
        
    with open('../../PyCopyCat/file1_dump.py') as file_1, open('../../PyCopyCat/file2_dump.py') as file_2:
        file1_data = file_1.read()
        file2_data = file_2.read()

        #Percentage/Ratio
        similarity_ratio = format(SequenceMatcher(None,file1_data,file2_data).ratio()*100,'.2f')
        #print(similarity_ratio)

    file_1='file1.py' #File name to display on the results page
    file_2='file2.py' #File name to display on the results page  

    #Removing Comments
    with open('../../PyCopyCat/file1.py', 'r')as f1:
        with open('../../PyCopyCat/prunedfile1.py','wt') as file1:
            for line in f1:
                if not line.strip().startswith('#'):
                    file1.write(line)
            file1.close()
    with open('../../PyCopyCat/file2.py', 'r')as f2:
        with open('../../PyCopyCat/prunedfile2.py','wt') as file2:
            for line in f2:
                if not line.strip().startswith('#'):
                    file2.write(line)
            file2.close()

    file1_lines = open('../../PyCopyCat/prunedfile1.py', 'r').readlines()
    file2_lines= open('../../PyCopyCat/prunedfile2.py', 'r').readlines()

    #Getting side by side comparison of 2 file contents
    diff_html_unformatted = difflib.HtmlDiff().make_table(file1_lines, file2_lines, file_1, file_2)
    
    #Result page
    return render(request, 'report1.html', {'data':similarity_ratio,'diff_html_table':diff_html_unformatted})


# File-Folder_Files comparison
def percent2(request):
   
    multi_files()
    with open('../../PyCopyCat/file1_dump.py') as file_1,open('../../PyCopyCat/file2_dump.py') as file_2:
        file1_data = file_1.read()
        file2_data = file_2.read()
        #Percentage/Ratio
        similarity_ratio = format(SequenceMatcher(None,file1_data,file2_data).ratio()*100,'.2f')
        #print(similarity_ratio)
    file_1='file1.py'   #File name to display on the results page
    file_2='file2.py'   #File name to display on the results page

    #Removing Comments
    with open('../../PyCopyCat/file1.py', 'r')as f1:
        with open('../../PyCopyCat/prunedfile1.py','wt') as file1:
            for line in f1:
                if not line.strip().startswith('#'):
                    file1.write(line)
            file1.close()
    with open('../../PyCopyCat/file2.py', 'r')as f2:
        with open('../../PyCopyCat/prunedfile2.py','wt') as file2:
            for line in f2:
                if not line.strip().startswith('#'):
                    file2.write(line)
            file2.close()

    file1_lines = open('../../PyCopyCat/prunedfile1.py', 'r').readlines()
    file2_lines= open('../../PyCopyCat/prunedfile2.py', 'r').readlines()
    
    #Getting side by side comparison of 2 file contents
    diff_html_unformatted = difflib.HtmlDiff().make_table(file1_lines, file2_lines, file_1, file_2)
    
    #Result page
    return render(request, 'report2.html', {'data':similarity_ratio,'diff_html_table':diff_html_unformatted})


# Folder-Files comparison
def percent3(request):
   
    folder_match()
    with open('../../PyCopyCat/file1_dump.py') as file_1,open('../../PyCopyCat/file2_dump.py') as file_2:
        file1_data = file_1.read()
        file2_data = file_2.read()
        
        #Percentage/Ratio
        similarity_ratio = format(SequenceMatcher(None,file1_data,file2_data).ratio()*100,'.2f')
        #print(similarity_ratio)
    file_1='file1.py'   #File name to display on the results page
    file_2='file2.py'   #File name to display on the results page

    #Removing Comments
    with open('../../PyCopyCat/file1.py', 'r')as f1:
        with open('../../PyCopyCat/prunedfile1.py','wt') as file1:
            for line in f1:
                if not line.strip().startswith('#'):
                    file1.write(line)
            file1.close()
    with open('../../PyCopyCat/file2.py', 'r')as f2:
        with open('../../PyCopyCat/prunedfile2.py','wt') as file2:
            for line in f2:
                if not line.strip().startswith('#'):
                    file2.write(line)
            file2.close()

    file1_lines = open('../../PyCopyCat/prunedfile1.py', 'r').readlines()
    file2_lines= open('../../PyCopyCat/prunedfile2.py', 'r').readlines()
    
    #Getting side by side comparison of 2 file contents
    diff_html_unformatted = difflib.HtmlDiff().make_table(file1_lines, file2_lines, file_1, file_2)
    
    #Result page
    return render(request, 'report3.html', {'data':similarity_ratio,'diff_html_table':diff_html_unformatted})
