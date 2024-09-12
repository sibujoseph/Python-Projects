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

        
    def isInterleave1(self, s1, s2, s3):
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
        

    def isInterleave(self, s1, s2, s3):
        
        NewS1=s1=aa
        NewS2=s2=ab
        NewS3=s3=aaba
        n=i=0
        rcp=[]

>>1
        NewS1=aa
        NewS2=ab
        NewS3=aaba
        rcp=0,s1>>a,aa,ab,aaba,Y,N 
        NewS1=a
        NewS2=ab
        NewS3=aba
        i=1
>>2
        NewS1=a
        NewS2=ab
        NewS3=aba
        rcp=1,s1>>a,a,ab,aba,Y,N 
        NewS1=
        NewS2=ab
        NewS3=ba
        i=2
>>3
        NewS1=
        NewS2=ab
        NewS3=ba
        retraction i=1 where retraction=Y, reversed=N
        reversed=Y
        rcp=1,s1>>a,a,ab,aba,Y,Y
        NewS1=a
        NewS2=ab
        NewS3=aba
        i=1
>>4
        NewS1=a
        NewS2=ab
        NewS3=aba
        rcp=1,s2>>a,a,ab,aba,Y,N
        NewS1=a
        NewS2=b
        NewS3=ba
        i=2
>>5
        NewS1=a
        NewS2=b
        NewS3=ba
        rcp=2,s2>>b,a,b,ba,Y,N
        NewS1=a
        NewS2=
        NewS3=a
        i=3
>>5
        NewS1=a
        NewS2=
        NewS3=a
        rcp=3,s1>>a,a,,a,Y,N
        NewS1=
        NewS2=
        NewS3=
        i=4
        
Done

        {
            get i>>i, rcp, s1>>NewS1, s2>>NewS2, s3>>NewS3
            
            NewS1n=take n of NewS1 until NewS1<>"" == NewS3n ? x=Y/N
            NewS2n=take n of NewS2 until NewS2<>"" == NewS3n ? y=Y/N
            
            if NewS1n=NewS2n then conflict
            
            #choose between NewS1n and NewS2n
            if x
                x-path=choose NewS1n if (NewS1n,NewS1,NewS2,NewS3) not in rcp
            if y
                y-path=choose s2n if not chosen x-path already and (NewS2n,NewS1,NewS2,NewS3) not in rcp
                        
            if x and y
                rcp >> retractable=Y, reversed=N
            else
                rcp >> retractable=N, reversed=N
            
            if not x and not y and (NewS1<>"" or NewS2<>"") and NewS3<>""
                i=last i of rcp where retraction=Y and reversed=N
                Update reversed=Y for respective rcp
                deduce NewS1=NewS1(i), NewS2=NewS2(i), NewS3=NewS3(i)
            else
                deduce NewS1=NewS1-NewS1n, NewS2=NewS2-NewS2n, NewS3=NewS3-NewS3n
                i+=1
            
            rcp or recent-chosen-path[+1]=x>>(i,NewS1n,NewS1,NewS2,NewS3) or y>>(i,NewS2n,NewS1,NewS2,NewS3) 
            (this becomes the array of retraction)
            
            apply function recurrsion >> input new (n, s1,s2,s3)
        }
"""
   
class Solution():

    r=Retractable=False
    depth=0
    rcp=[]
    
    def setReversed(self,rcp,n):
        newrcp=[]
        #print("in>>n",n)
        #print("setReversed>>depth>>",self.depth, "rcp in>>",self.rcp,"len(rcp)>>",len(rcp))
        n=len(rcp)-n
        #print("out>>n",n)
        for (i,v) in enumerate(rcp):
            #print("i>>",i)
            Reversed=True if i>=n else False
            #print(v)
            newrcp.append((v[0],v[1],v[2],v[3],v[4],v[5],Reversed))
        
        self.rcp=newrcp
        #print("setReversed>>depth>>",self.depth, "rcp out>>",self.rcp)
        return self.rcp

    def RCPExists(self,rcp,xy):
        Flag=False
        i=0
        for (i,v) in enumerate(rcp):
            #print("RCPExists>>depth>>",self.depth,"v>>",v,"xy>>",xy)
            if v==xy:
                Flag=True
        #print("RCPExists>>depth>>",self.depth,"rcp>>",rcp,"Check if",xy,"Exists in rcp>>",Flag)
        return Flag
    
    def RetractRCP(self,rcp):
        n=0
        for i in reversed(rcp):
            n+=1
            if i[5]==True and i[6]==False:
                #print("retracted>>",i)
                break
        #Reversed
        self.setReversed(rcp,n)
        #print("RetractRCP>>depth>>",self.depth, (i[2],i[3],i[4]))
        return (i[2],i[3],i[4])


    def StringMapper(self, rcp, s1, s2, s3):

        chosen=""
        news1=news2=news3=""
        
        self.depth+=1
        #print("depth>>",self.depth)
        if self.depth>10:
            exit
        
        if s1!="":
            if s1[0]==s3[0] and not self.RCPExists(self.rcp, ("s1",s1[0],s1,s2,s3,True,True)):
                news1=s1[1:]
                news2=s2
                news3=s3[1:]
                chosen="s1"
                #print("test1>>in>>[", s1, s2, s3, "] out>>", news1,news2,news3)

        if s2!="":
            if s2[0]==s3[0] and chosen=="" and not self.RCPExists(self.rcp, ("s2",s2[0],s1,s2,s3,True,True)):
                news1=s1
                news2=s2[1:]
                news3=s3[1:]
                chosen="s2"
                #print("test2>>in>>[", s1, s2, s3, "] out>>", news1,news2,news3)
        
        if s1!="" and s2!="" and chosen!="":
            #conflict
            Retractable=True if s1[0]==s2[0] else False 
        else:
            Retractable=False
        
        self.rcp.append((chosen,s3[0],s1,s2,s3,Retractable,False))
        #print("StringMapper>>test3>>depth>>",self.depth,"rcp>>",self.rcp)
    
        if chosen=="" and (s1!="" or s2!="") and s3!="":
            #print("StringMapper>>test4>>depth>>",self.depth,">>retraction>>in>>", s1, s2, s3, news1,news2,news3)
            (news1,news2,news3)=self.RetractRCP(self.rcp)  #Retracted s1 s2 s3
            #print("StringMapper>>test5>>depth>>",self.depth,"retraction>>out>>", s1, s2, s3, news1,news2,news3)

        if news1=="" and news2=="" and news3=="":
            self.r=True
            #print("StringMapper>>test6>>depth>>",self.depth,"r>>", self.r)
        else:
            #print("StringMapper>>test7>>depth>>",self.depth,">>recursion>>rcp>>",self.rcp, news1, news2, news3)
            self.StringMapper(self.rcp, news1, news2, news3)

        return self.r


    def isInterleave(self, s1, s2, s3):
        
        self.StringMapper(self.rcp, s1, s2, s3)

        



if __name__ == "__main__":
    
    s1="aa"
    s2="ab"
    s3="aaba"
    
    #print("s1:",s1,"s2:",s2,"s3:",s3)
    
    x=Solution()
    print(x.isInterleave(s1, s2, s3))
