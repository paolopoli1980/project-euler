# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:33:02 2016

@author: paolo
"""
def dynamicalgo():
    
    som=0
    
    for i in range(98,-1,-1):
      #  print i
        
        for j in range(i):
            if matrix[i+1][j+1]>matrix[i+1][j]:
                matrix[i][j]=matrix[i+1][j+1]+matrix[i][j]
            else:
                matrix[i][j]=matrix[i+1][j]+matrix[i][j]
                
    som = max(matrix[1])
    return som+matrix[0][0]            
    
def maximum():
    som=0
    for i in range(100):
        maxx=0
        for j in range(len(matrix[i])):
            if matrix[i][j]>maxx:
                maxx=matrix[i][j]
            
                
        som=som+maxx
    return som        
def gredy():
    som=matrix[0][0]
    memx=0
    for i in range(1,100):
        if matrix[i][memx]>matrix[i][memx+1]:
            som=som+matrix[i][memx]
        else:
            som=som+matrix[i][memx+1]
            memx+=1
    return som        
f1=open("p067_triangle.txt")

stringa="*"
lista=[]

while stringa!="":
    stringa=f1.readline()
    lista.append(stringa)
     
matrix=[[0 for i in range(100)]for j in range(100)]
matrixinc=[[0 for i in range(100)]for j in range(100)]

for i in range (100):
    stringa=lista[i].split()
    for j in range(len(stringa)):
        matrix[i][j]=int(stringa[j])

print matrix   

print gredy()
print maximum()
print dynamicalgo()


     
f1.close()    