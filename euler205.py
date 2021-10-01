# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 11:49:14 2016

@author: paolo
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""
import math
max1=600000
max2=9000
listcomb1=[]
listcomb2=[]
for i in range(max1+1):
    stringa=str(i)
    som=0
    if len(str(i))==1:
        stringa=str('00000')+stringa
    if len(str(i))==2:
        stringa=str('0000')+stringa
    if len(str(i))==3:
        stringa=str('000')+stringa
    if len(str(i))==4:
        stringa=str('00')+stringa
    if len(str(i))==5:
        stringa=str('0')+stringa
        
    for el in stringa:
        som+=int(el)
    if som==6:
        listcomb1.append(stringa)
            
for i in range(max2+1):
    stringa=str(i)
    som=0
    if len(str(i))==1:
        stringa=str('000')+stringa
    if len(str(i))==2:
        stringa=str('00')+stringa
    if len(str(i))==3:
        stringa=str('0')+stringa

    for el in stringa:
        som+=int(el)
    if som==9:
        listcomb2.append(stringa)
            
print listcomb1
print listcomb2            
cont=0

res2=[]
numb=[0,0,0,0]
res2rip=[]
for el in listcomb2:
    numb=[0,0,0,0]

    cont=0
    som=0
    n=0
    for elx in el:
        cont+=1
        som=som+int(elx)*cont
        numb[cont-1]=int(elx)
    res2.append(som)
    n=math.factorial(9)/(math.factorial(numb[0])*math.factorial(numb[1])*math.factorial(numb[2])*math.factorial(numb[3]))
    res2rip.append(n)    
res1=[]
res1rip=[]
    
for el in listcomb1:
    numb2=[0,0,0,0,0,0]

    cont=0
    som=0
    n=0
    for elx in el:
        cont+=1
        som=som+int(elx)*cont
        numb2[cont-1]=int(elx)
    res1.append(som)
    n=math.factorial(6)/(math.factorial(numb2[0])*math.factorial(numb2[1])*math.factorial(numb2[2])*math.factorial(numb2[3])*math.factorial(numb2[4])*math.factorial(numb2[5]))
    res1rip.append(n)    
p1=0 
for i in range(len(res2)):
    for j in range(len(res1)):
        if res2[i]>res1[j]:
            p1+=res2rip[i]*res1rip[j]
            
sx=0            
for i in range(len(res1rip)):
    for j in range(len(res2rip)):
        sx+=res1rip[i]*res2rip[j]
  

print sx    
    
print res2
print res1
print res2rip
print p1
print sx
print float(float(p1)/float(sx))
#print float(p1)/float((6**6*4**9))
sx=0
         
    
