# For comparing files in a folder 
import glob
import ast
import os
from difflib import SequenceMatcher
def folder_match():
    class Compare2:
        
            
        def match(self):
            os.chdir('D:/Hudl/Madhu/final project/PyCopyCat/upload')
            files=glob.glob('*.py')
            num_files=len(files)
            cnt1=0
            cnt2=1
            cnt3=0
            cnt4=0
            i=0
            a=[]
            limit=0.0
            print(files)
            l=[ ]
            del l[:]
            while True:
                if cnt1<num_files:
                    #Genreating AST for folder files
                    file1=ast.parse(open(files[cnt1]).read())
                    file1_dump=ast.dump(file1)
                    
                    #with open('../../PyCopyCat/file1_dump.py','wt')as f1:
                     #   f1.write(file1_dump)
                    
                    if cnt2<num_files:
                        file2=ast.parse(open(files[cnt2]).read())
                        file2_dump=ast.dump(file2)
                        similarity_ratio = format(SequenceMatcher(None,file1_dump,file2_dump).ratio()*100,'.2f')
                        str_to_flt=float(similarity_ratio)
                        #print(str_to_flt)
                        if str_to_flt>limit:
                            for wrt in range(1) :
                                l.append(files[cnt1]+' is compared with '+files[cnt2]+' percentage is: {0}'.format(str_to_flt))
                            #print(files[cnt1],'is cmp with',files[cnt2], 'percentage ',str_to_flt)
                            if i == cnt4:    
                                a.append(str_to_flt)
                                i+=1
                            cnt2+=1
                            cnt4+=1
                        else:
                            pass
                            break
                    else:
                        
                        cnt3+=1
                        cnt2=cnt3+1
                        cnt1+=1

                        
                else:
                     
                    break 
            percentage_values=a
            #print(percentage_values)
            self.max_percentage=max(percentage_values, default=0)
            #print(max_percentage)
            with open('../../PyCopyCat/match2.txt','wt')as f2:
                        for listitem in l:
                            f2.write('%s\n' % listitem)
                        
                        f2.close() 
             
     
        def folder_files(self):
            os.chdir('D:/Hudl/Madhu/final project/PyCopyCat/upload')
            files=glob.glob('*.py')
            num_files=len(files)
            cnt1=0
            cnt2=1
            cnt3=0
            limit=70.0
            print(files)
            
            while True:
                if cnt1<num_files:
                    #file2_content=open(files[cnt],'r')
                    file1=ast.parse(open(files[cnt1]).read())
                    file1_dump=ast.dump(file1)
                    #similarity_ratio = format(SequenceMatcher(None,file1_dump,file2_dump).ratio()*100,'.2f')
                    #str_to_flt=float(similarity_ratio)
                    with open('../../PyCopyCat/file1_dump.py','wt')as f1:
                        f1.write(file1_dump)
                    with open(files[cnt1],'r') as f:
                        with open("../../PyCopyCat/file1.py", "wt") as f1:
                            for line in f:
                                f1.write(line)
                            f1.close()
                    #print(files[cnt1])
                    #print(cnt2) 
                    if cnt2<num_files:
                        file2=ast.parse(open(files[cnt2]).read())
                        file2_dump=ast.dump(file2)
                        similarity_ratio = format(SequenceMatcher(None,file1_dump,file2_dump).ratio()*100,'.2f')
                        str_to_flt=float(similarity_ratio)
                        #print(str_to_flt)
                        if self.max_percentage!= str_to_flt:
                            #print(files[cnt1],'is cmp with',files[cnt2], 'percentage ',str_to_flt)
                            cnt2+=1

                        else:
                            #file1 and file2 comparison max percentage that file is written onto file2
                            with open(files[cnt2],'r') as f:
                                    with open("../../PyCopyCat/file2.py", "wt") as f1:
                                        for line in f:
                                            f1.write(line)
                                        f1.close()
                            print(files[cnt1],'is matched with',files[cnt2],' percentage ',str_to_flt)
                            with open('../../PyCopyCat/file2_dump.py','wt')as f2:
                                f2.write(file2_dump)
                                #print(file2_dump)
                            break
                    else:
                        print(files[cnt1],'is not matched with any of the files ')
                        cnt3+=1
                        cnt2=cnt3+1
                        #print('cnt2 is',cnt2)
                        #break
                        cnt1+=1
                        #print('cnt1 is',cnt1)
                        #print("next file")
                else:
                    print('No files are similar') 
                    break       

                    
    s=Compare2()
    s.match()
    s.folder_files()           
folder_match() 
 