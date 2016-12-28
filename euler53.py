# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:26:59 2016

@author: paolo
"""
import math
def binomial(i,j):
    
    x=math.factorial(i)
    y=math.factorial(j)
    z=math.factorial(i-j)
    return x/(y*z)
    

lista=[]
c=0
n=101
l=1000000

for i in range(n):
    print "*"
    for j in range(i):
        if binomial(i,j)>l:
            c+=1
        print binomial(i,j)
print c