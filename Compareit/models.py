from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
class File1(models.Model):
    firstfile=models.CharField(max_length=1000,blank=True,unique=True, default="")
    #secondfile=models.CharField(max_length=1000)
    def __str__(self):
        return self.firstfile
class File2(models.Model):
    secondfile = models.CharField(max_length=1000,blank=True, unique=True,default="")
    def __str__(self):
        return self.secondfile
"""
class Result(models.Model):
     #sno1=models.ForeignKey(File1,on_delete=models.CASCADE)
     #sno2=models.ForeignKey(File2, on_delete=models.CASCADE)
     sameprograms=models.CharField(max_length=50)
     percent=models.FloatField(max_length=10)

     def __str__(self):
         return  self.percent+ ' '+ self.sameprograms
class Result2(models.Model):
#sno1=models.ForeignKey(File1,on_delete=models.CASCADE)
#sno2=models.ForeignKey(File2, on_delete=models.CASCADE)
    sameprograms=models.CharField(max_length=50)
    percent=models.FloatField(max_length=10)
class Result3(models.Model):
#sno1=models.ForeignKey(File1,on_delete=models.CASCADE)
#sno2=models.ForeignKey(File2, on_delete=models.CASCADE)
    sameprograms=models.CharField(max_length=50)
    percent=models.FloatField(max_length=10)



def __str__(self):
    return  self.percent+ ' '+ self.sameprograms
