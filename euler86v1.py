# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 00:49:36 2016

@author: paolo
"""

import math
def f(x):
    f= (x/math.sqrt(x**2+ky**2)+(x-kx)/math.sqrt(kx**2+x**2-2*kx*x+kz**2))
  #  print kz
    return f

def g(x):
    g=math.sqrt(x**2+ky**2)+math.sqrt((kx-x)**2+kz**2)
  
    return g 
x=0
kx=0
ky=0
kz=0
s=0

k=0



for kx in range(1,10000):
    #print kx
    for ky in range(1,10000):
        if kz+ky>20000:
		ky=10000   	

        for kz in range(1,10000):
		
	    if kz+ky>20000:
		kz=10000     	
            if kz+ky<=20000 and ky<=kx and kz<=kx and ky>=kz:
             
                if abs(math.sqrt(kx**2+(ky+kz)**2)-int(math.sqrt(kx**2+(ky+kz)**2)))==0:
                    
                    no=0
                
                    if no==0:
                       s+=1
                    
	               if s>1000000:
		       		print "got it"
				print s
				print kx,ky,kz
				exit() 	
 
   
