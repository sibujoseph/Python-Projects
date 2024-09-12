# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 23:24:30 2021

@author: sibuj
"""
NewS3="Test"
NewS1="test"
ab="ab"
lenS1=len(NewS1)
print(lenS1)
        #s1
for (i, v1) in enumerate(NewS3):
    #print("S3", i,v1)
    if i<lenS1 and v1==NewS1[i]:
        #s1Flag=True
        print("S1",i,v1)
        print(NewS1[0:max(i,1)])
        print(NewS3[0:max(i,1)])
        print(NewS1[0:(i+1)])
        print(NewS3[0:(i+1)])
        
    #else:
    #    break
    
print(NewS3[3:])
print(ab[2:2])