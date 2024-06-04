#For comparing single file with multiple files
import glob
import ast
import os
from difflib import SequenceMatcher
def multi_files():
    class Compare:
        #global cnt,limit,a,i,num_files,files,file_1
        
        def match_value(self):
            os.chdir('D:/Hudl/Madhu/final project/PyCopyCat/upload')
            files=glob.glob('*.py')

            num_files=len(files)
        
            cnt=0
            limit=70.0
            a=[]
            i=0
            #print(files)
            #print('no of file',num_files)

            #Generating AST
            file1=ast.parse(open('../../PyCopyCat/file1.py').read())
            file1_dump=ast.dump(file1)
            with open('../../PyCopyCat/file1_dump.py','wt')as f1:
                f1.write(file1_dump) 
            l=[ ]
            del l[:]
            while True:
                if cnt<num_files:
                    #Genreating AST for folder files
                    file1=ast.parse(open(files[cnt]).read())
                    file2_dump=ast.dump(file1)
                    similarity_ratio = format(SequenceMatcher(None,file1_dump,file2_dump).ratio()*100,'.2f')
                    str_to_flt=float(similarity_ratio)
                    #comparison='file1 matched with '+files[cnt]+'  percentage is'+similarity_ratio+'%'

                    for wrt in range(1) :
                        l.append('file1 matched with '+files[cnt]+'  percentage is  {0}'.format(str_to_flt))
                    
                    #print('file1 matched with '+files[cnt]+'  percentage is  {0}'.format(str_to_flt))
                    if i == cnt:    
                        a.append(str_to_flt)
            
                        i+=1
                    cnt+=1

           
                else:
                    break

            percentage_values=a
            #print(percentage_values)
            self.max_percentage=max(percentage_values, default=0)
            #print(self.max_percentage)
            with open('../../PyCopyCat/match1.txt','wt')as f2:
                for listitem in l:
                    f2.write('%s\n' % listitem)
                
                f2.close()
            
            #print(l)

            
    #match_value()
        def compare_files(self):
            os.chdir('../../PyCopyCat/upload')
            files=glob.glob('*.py')

            num_files=len(files)
        
            cnt=0
            limit=70.0
            #a=[]
            i=0   
            file1=ast.parse(open('../../PyCopyCat/file1.py').read())
            file1_dump=ast.dump(file1)
            with open('../../PyCopyCat/file1_dump.py','wt')as f1:
                f1.write(file1_dump) 
            while True:#if self.max_percentage>limit:
                if cnt<num_files:
                    file1=ast.parse(open(files[cnt]).read())
                    file2_dump=ast.dump(file1)
                    similarity_ratio = format(SequenceMatcher(None,file1_dump,file2_dump).ratio()*100,'.2f')
                    str_to_flt=float(similarity_ratio)
                    
                     
                    if self.max_percentage!=str_to_flt:
                        cnt+=1
                        
                            

                    else:
                        #file1 and file2 comparison max percentage that file is written onto file2
                        with open(files[cnt],'r') as f:
                                with open("../../PyCopyCat/file2.py", "wt") as f1:
                                    for line in f:
                                        f1.write(line)
                                    f1.close()
                        print('file1 is matched with',files[cnt],' percentage ',str_to_flt)
                        with open('../../PyCopyCat/file2_dump.py','wt')as f2:
                                f2.write(file2_dump) 
                        break  
                    #print('value',cnt)
                    #print('file1 is matched with '+files[cnt]+'  percentage is ',self.max_percentage)
                    #cnt+=1      
                else:
                
                    print("NO file is matched")
                    break
                
            #else:
             #   print("No files matching percentage is greater than 70% ")
              #  print('So nothing of the file is matched')
    s=Compare()
    s.match_value()
    s.compare_files()
multi_files()