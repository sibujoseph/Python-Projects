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
    
    r=False

    def StringCompare(self, NewStrChild, NewStrMain):
        
        #print("IN>>",NewStrChild,NewStrMain)
        lenStrChild=len(NewStrChild)
        lenStrMain=len(NewStrMain)
        fetchChar=i=0
        StrChildExistsFlag=False

        for (i, v) in enumerate(NewStrMain):
            if i<lenStrChild and v==NewStrChild[i]:
                fetchChar+=1
                StrChildExistsFlag=True
            else:
                break
            
        if fetchChar==lenStrMain:
            i+=1

        if StrChildExistsFlag==True: 
            NewStrChild=NewStrChild[i:lenStrChild] if lenStrChild>1 else ""
            NewStrMain=NewStrMain[i:lenStrMain] if lenStrMain>1 else ""
        
        fetchChar=0
        
        #print("OUT>>",NewStrChild,NewStrMain)
        return NewStrChild,NewStrMain,len(NewStrChild),len(NewStrMain)

        
        
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        NewS1=s1
        NewS2=s2
        NewS3=s3

        #s1
        (NewS1, NewS3, lenS1, lenS3)=self.StringCompare(NewS1, NewS3)
        #s2
        (NewS2, NewS3, lenS2, lenS3)=self.StringCompare(NewS2, NewS3)

        if len(NewS3)>0 and NewS1!=s1 and NewS2!=s2: 
            self.isInterleave(NewS1, NewS2, NewS3)
        
        #print(lenS1, lenS2, lenS3)
        if lenS1==0 and lenS2==0 and lenS3==0:
            self.r=True
        
        return self.r
        

if __name__ == "__main__":
    
    s1=""
    s2=""
    s3=""
    
    #print("s1:",s1,"s2:",s2,"s3:",s3)
    
    x=Solution()
    print(x.isInterleave(s1, s2, s3))
