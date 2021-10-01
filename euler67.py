# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:33:02 2016

@author: paolo

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
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
