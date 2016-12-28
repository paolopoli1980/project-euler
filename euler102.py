# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:25:43 2016

@author: paolo
"""
class triangle:
    
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1=float(x1)
        self.y1=float(y1)
        self.x2=float(x2)
        self.y2=float(y2)
        self.x3=float(x3)
        self.y3=float(y3)
        
        
f1=open("p102_triangles.txt","r")

stringa="*"
obj=[]
while stringa!="":
 
    stringa=f1.readline()
    if stringa!="":
        print stringa+str("\n")
        x1,y1,x2,y2,x3,y3=stringa.split(",")
        print x1,y1,x2,y2,x3,y3
        obj.append(triangle(x1,y1,x2,y2,x3,y3))
   
lista=[]        
cont=0
#obj.append(triangle(-340,495,-153,-910,835,-947))
#obj.append(triangle(-175,41,-421,-714,574,-645))

for i in obj:

    print i.x1
    print i.y1
    print i.x2
    print i.y2
    print i.x3
    print i.y3

    d21x=i.x2-i.x1
    d21y=i.y2-i.y1
    d31x=i.x3-i.x1
    d31y=i.y3-i.y1
    d32x=i.x3-i.x2
    d32y=i.y3-i.y2
    print d21x,d21y,d31x,d31y,d32x,d32y
    lim=100000000000000000000
    if d21x==0:
        t1x=lim
    if d21y==0:
        t1y=lim
    if d31x==0:
        t2x=lim
    if d31y==0:
        t2y=lim
    if d32x==0:
        t3x=lim
    if d32y==0:
        t3y=lim
        
        

   # d21x*t+i.x1=0
    mx1=lim
    mx2=lim
    mx3=lim
    my1=lim
    my2=lim
    my3=lim

    if d21x!=0:
        t1x=-i.x1/d21x
     
    if (t1x>=0 and t1x<=1):
        mx1=d21y*t1x+i.y1
    if d21y!=0:

        t1y=-i.y1/d21y

    if (t1y>=0 and t1y<=1):
        my1=d21x*t1y+i.x1
        
    if d31x!=0:

        t2x=-i.x1/d31x

    if (t2x>=0 and t2x<=1):
        mx2=d31y*t2x+i.y1

    if d31y!=0:

        t2y=-i.y1/d31y
    if (t2y>=0 and t2y<=1):
        my2=d31x*t2y+i.x1
    if d32x!=0:
  
        t3x=-i.x2/d32x
    if (t3x>=0 and t3x<=1):
        mx3=d32y*t3x+i.y2

    if d32y!=0:
 
        t3y=-i.y2/d32y
    if (t3y>=0 and t3y<=1):
        my3=d32x*t3y+i.x2
    listax=[mx1,mx2,mx3]
    listay=[my1,my2,my3]
    print listax
    print listay
    
         
    okx=0
    oky=0 
#    cont=0    
    for j in range(len(listax)):
        for i in range (j+1,len(listax)):
            if listax[i]*listax[j]<=0 and listax[i]<lim and listax[j]<lim:
                okx=1
    for j in range(len(listay)):
        for i in range (j+1,len(listay)):
            if listay[i]*listay[j]<=0 and listay[i]<lim and listay[j]<lim:
                oky=1
    if okx==1 and oky==1:
        cont+=1
print cont
print len(obj)
                
            


        