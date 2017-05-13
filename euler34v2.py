# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:09:11 2017

@author: paolo
"""

import math

lim1=1
lim2=999999
cont=0
som=0
fivefac=math.factorial(5)
sixfac=math.factorial(6)
sevenfac=math.factorial(7)
onefac=math.factorial(1)
eightfac=math.factorial(8)
ninefac=math.factorial(9)
twofac=math.factorial(2)
threefac=math.factorial(3)
fourfac=math.factorial(4)
 
for i in range(lim1,lim2):
    string=str(i)
    som=0
    for el in string:
        if el=='0':
            som+=1

        if el=='1':
            som+=onefac
        if el=='2':
            som+=twofac
        if el=='3':
            som+=threefac
        if el=='4':
            som+=fourfac
        if el=='5':
            som+=fivefac
        if el=='6':
            som+=sixfac
        if el=='7':
            som+=sevenfac
        if el=='8':
            som+=eightfac
        if el=='9':
            som+=ninefac
             
    if som==i:
        cont+=som
        print i
print cont    
 