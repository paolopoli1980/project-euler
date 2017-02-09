# -*- coding: utf-8 -*-
"""
Created on Fri Dec 06 22:00:42 2013

@author: paolo
"""


def control(stringa):
    warn=0    
    for el in val:
       # print(el)
        conta=0
        contaold=0
        contac=0
        for c in el:
                        
            
            conta=0
            for  cc in stringa:
                conta=conta+1                
                if (cc==c) and (conta>contaold):
                    contac=contac+1
                    contaold=conta
                    break                    
        if contac<3:
            warn=1
            break
    if warn==0:
        print(stringa)
        exit()
                        
f1=open('testo.txt','r')
val=[]
stringa="1"
while stringa!="":
    
    stringa=f1.readline()
    if stringa!="":
        val.append(stringa[0:3])
    #print(stringa)    
print(val)        

#control('30126789')
#exit()
lista1=[3,6,7,8,9]
lista2=[i for i in range(10)]
lista2.remove(4)
lista2.remove(5)

lista3=lista2[:]
lista4=lista2[:]
lista5=lista2[:]
lista6=lista2[:]
lista7=lista2[:]
lista8=lista2[:]


#print lista2
for e1 in lista1:
    for e2 in lista2:
        for e3 in lista3:
            for e4 in lista4:
                for e5 in lista5:
                    for e6 in lista6:
                        for e7 in lista7:
                            for e8 in lista8:
                                stringa=str(e1)+str(e2)+str(e3)+str(e4)+str(e5)+str(e6)+str(e7)+str(e8)
                                control(stringa)        
    #print(stringa)