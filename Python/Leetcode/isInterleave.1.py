# -*- coding: utf-8 -*-
"""
@author: sibuj

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution(object):
    
    depth=0
    mapper=[]
    r=False

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1Flag=s2Flag=False 
        NewS1=s1
        NewS2=s2
        NewS3=s3
 
        lenS1=len(NewS1)
        lenS2=len(NewS2)
        lenS3=len(NewS3)
        
        fetchChar=i=j=0
       
        if self.depth>=0:
            print("depth:{} >>1>> NewS1:{}, NewS2:{}, NewS3:{}".format(self.depth, NewS1, NewS2, NewS3))
        
        #s1
        for (i, v1) in enumerate(NewS3):
            if i<lenS1 and v1==NewS1[i]:
                fetchChar+=1
                print(i, fetchChar)
                s1Flag=True
            else:
                break
            
        if fetchChar==lenS3:
            i+=1 
            
        if s1Flag==True: 
            self.mapper.append((NewS3[0:fetchChar],"->S1:"+NewS1[0:fetchChar]))
            #self.mapper.append((NewS3[0:max(i,1)],"->S1:"+NewS1[0:max(i,1)]))
            print("i>>", i, "mapper:{}".format(self.mapper), "s1Flag: ", s1Flag, lenS1, lenS3)
            NewS1=NewS1[i:lenS1] if lenS1>1 else ""
            NewS3=NewS3[i:lenS3] if lenS3>1 else ""
            lenS1=len(NewS1)
            lenS3=len(NewS3)
            print("i=",i, "lenS1=",lenS1, "lenS3=",lenS3, "NewS1=",NewS1, "NewS3=",NewS3)
        
        fetchChar=0
        
        if self.depth>=0:
            print("depth:{} >>2>> NewS1:{}, NewS2:{}, NewS3:{}".format(self.depth, NewS1, NewS2, NewS3))
        #s2
        for (j, v2) in enumerate(NewS3):
            if j<lenS2 and v2==NewS2[j]:
                fetchChar+=1
                print(j, fetchChar)
                s2Flag=True
            else:
                break
        
        if fetchChar==lenS3:
            j+=1 

        if s2Flag==True: 
            self.mapper.append((NewS3[0:fetchChar],"->S2:"+NewS2[0:fetchChar]))
            #self.mapper.append((NewS3[0:max(j,1)],"->S2:"+NewS2[0:max(j,1)]))
            print("j>>",j, "mapper:{}".format(self.mapper), "s2Flag: ", s2Flag, lenS2, lenS3)
            NewS2=NewS2[j:lenS2] if lenS2>1 else ""
            NewS3=NewS3[j:lenS3] if lenS3>1 else ""
            lenS2=len(NewS2)
            lenS3=len(NewS3)
            print("j>>",j, "lenS2=",lenS2, "lenS3=",lenS3, "NewS2=",NewS2, "NewS3=",NewS3)


        if self.depth>=0:
            print("depth:{} >>3>> NewS1:{}, NewS2:{}, NewS3:{}".format(self.depth, NewS1, NewS2, NewS3))
        if len(NewS3)>0 and NewS1!=s1 and NewS2!=s2 and self.depth<10:
            self.depth+=1
            self.isInterleave(NewS1, NewS2, NewS3)
        
        print(self.depth,lenS1,lenS2,lenS3)
        if lenS1==0 and lenS2==0 and lenS3==0:
            self.r=True
        
        return self.r
        

if __name__ == "__main__":
    
    s1="aaba"
    s2="ab"
    s3="aaabba"
    
    print("s1:",s1,"s2:",s2,"s3:",s3)
    
    x=Solution()
    x.depth=0
    print(x.isInterleave(s1, s2, s3))
