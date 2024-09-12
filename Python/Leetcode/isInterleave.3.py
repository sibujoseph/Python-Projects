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
    
    def StringMapper(self, NewStrChild, NewStrMain):

        lenStrChild=len(NewStrChild)
        lenStrMain=len(NewStrMain)
        fetchChar=i=0

        for (i, v) in enumerate(NewStrMain):
            if i<lenStrChild and v==NewStrChild[i]:
                fetchChar+=1
            else:
                break
        
        #print("StringMapper>>", i, fetchChar, lenStrChild, lenStrMain)
        return i, fetchChar, lenStrChild, lenStrMain

        
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
        fetch1=fetch2=lenS1=lenS2=lenS3=0

        #print("IN>>",s1,s2,s3)

        #s1
        (i, fetch1, lenS1, lenS3)=self.StringMapper(NewS1,NewS3)
        #s2
        (j, fetch2, lenS2, lenS3)=self.StringMapper(NewS2,NewS3)
        
        if fetch1>fetch2:
            #print("1 wins")
            if fetch1==lenS3:
                i+=1
            NewS1=NewS1[i:lenS1] if lenS1>1 else ""
            NewS3=NewS3[i:lenS3] if lenS3>1 else ""

        if fetch2>fetch1:
            #print("2 wins")
            if fetch2==lenS3:
                j+=1
            NewS2=NewS2[j:lenS2] if lenS2>1 else ""
            NewS3=NewS3[j:lenS3] if lenS3>1 else ""

        #print("OUT>>",NewS1, NewS2, NewS3)

        if len(NewS3)>0 and (NewS1!=s1 or NewS2!=s2): 
            self.isInterleave(NewS1, NewS2, NewS3)
        
        if NewS1=="" and NewS2=="" and NewS3=="":
            self.r=True
        
        return self.r
        

if __name__ == "__main__":
    
    s1="aa"
    s2="ab"
    s3="aaba"
    
    #print("s1:",s1,"s2:",s2,"s3:",s3)
    
    x=Solution()
    print(x.isInterleave(s1, s2, s3))
