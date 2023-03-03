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
   
class Solution():

    Retractable=False
    depth=0
    rcp=[]
    

    def AlreadyExistsInRCP(self,rcp,xy):
        Flag=False
        i=0
        for (i,v) in enumerate(rcp):
            if v==xy:
                Flag=True
        return Flag
    
    
    def RetractRCP(self,rcp):
        n=0
        newrcp=[]
        for i in reversed(rcp):
            n+=1
            if i[5]==True and i[6]==False:
                break
        
        #Reverse rcp to last Retractable point
        for (j,v) in enumerate(rcp):
            Reversed=True if j>=(len(rcp)-n) else v[6]
            Retractable=False if j>=(len(rcp)-n) else v[5]
            newrcp.append((v[0],v[1],v[2],v[3],v[4],Retractable,Reversed))
        
        self.rcp=newrcp        
        
        return (i[2],i[3],i[4])


    def StringMapper(self, rcp, s1, s2, s3):

        chosen=""
        news1=news2=news3=""
        
        #debug
        self.depth+=1
        #if self.depth>10:
        #    exit
        
        if s1!="":
            if s1[0]==s3[0] and not self.AlreadyExistsInRCP(self.rcp, ("s1",s1[0],s1,s2,s3,False,True)):
                news1=s1[1:]
                news2=s2
                news3=s3[1:]
                chosen="s1"

        if s2!="":
            if s2[0]==s3[0] and chosen=="" and not self.AlreadyExistsInRCP(self.rcp, ("s2",s2[0],s1,s2,s3,False,True)):
                news1=s1
                news2=s2[1:]
                news3=s3[1:]
                chosen="s2"
        
        if chosen!="":
            #conflict
            Retractable=True if (s1!="" and s2!="" and s1[0]==s2[0]) else False 
            self.rcp.append((chosen,s3[0],s1,s2,s3,Retractable,False))
        
        #if self.depth>=20: 
        print("depth>>",self.depth,"rcp>>",self.rcp)
        #exit
    
        if chosen=="" and (s1!="" or s2!="") and s3!="":
            (news1,news2,news3)=self.RetractRCP(self.rcp)  #Retracted s1 s2 s3

        if (news1!="" or news2!="") and news3!="": #Recursive call
            self.StringMapper(self.rcp, news1, news2, news3)

        if news1=="" and news2=="" and news3=="":
            self.r=True

        return self.r


    def isInterleave(self, s1, s2, s3):
        
        return self.StringMapper(self.rcp, s1, s2, s3)

        



if __name__ == "__main__":
    
    s1="aaa"
    s2="abba"
    s3="aababaac"

    s1="aabcc"
    s2="dbbca"
    s3="aadbbbaccc"
    

    #print("s1:",s1,"s2:",s2,"s3:",s3)
    
    x=Solution()
    x.r=False
    print(x.isInterleave(s1, s2, s3))
