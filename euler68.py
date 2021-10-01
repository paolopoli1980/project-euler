# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 21:46:43 2016

@author: paolo

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
"""
import permutdef

#euler 68
graf=[0,0,0,0,0,0,0,0,0,0]
lista=[]
lista[:]=permutdef.permuta()
n=[0,0,0,0,0]

print ("start")
maxtot=0
for el in lista:
    cont=0
   # print cont
    for elx in el:
        if elx!='a':
            graf[cont]=int(elx)

        if elx=='a':
            graf[cont]=10
        
            
        cont+=1
        
    n[0]=str(graf[0])+str(graf[5])+str(graf[6])
    n[1]=str(graf[1])+str(graf[6])+str(graf[7])        
    n[2]=str(graf[2])+str(graf[7])+str(graf[8])
    n[3]=str(graf[3])+str(graf[8])+str(graf[9])
    n[4]=str(graf[4])+str(graf[9])+str(graf[5])
    c=-1
    minn=1000000000000000
    num=0
    for el in n:
        c+=1
        if int(el)<minn:
            minn=int(el)
            num=c
    c=num-1
    n2=[]            
    for el in n:
       c+=1
       if c==5:
           c=0
       n2.append(n[c])
    n[0]=n2[0]
    n[1]=n2[1]
    n[2]=n2[2]
    n[3]=n2[3]
    n[4]=n2[4]

       
    if n[0][1]=='0' or n[1][1]=='0' or n[2][1]=='0' or n[3][1]=='0' or n[4][1]=='0':                     
       
        somma=[0,0,0,0,0]
        for j in range(5):
          
            for i in range(len(n[j])):
                id=0
                if i!=len(n[j])-1:
                    if n[j][i]=='1' and n[j][i+1]=='0':
                        somma[j]+=10
                        id=1
                        i+=1
                if id==0:        
                    somma[j]+=int(n[j][i])
            
        error=0
                    
        for i in range(5):
            for j in range(i+1,5):
                if somma[i]!=somma[j]:
    
                        error=1
                        
        if error==0:
            print ("processato")
            tot=str(n[0])+str(n[1])+str(n[2])+str(n[3])+str(n[4])
            
            if int(tot)>int(maxtot):
                maxtot=tot
print (maxtot)
                   
        
    
    
