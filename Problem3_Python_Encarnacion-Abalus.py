# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 01:33:02 2019

@author: ENCARNACION & ABALUS
"""

def f(x):
    a = x**2+x+1
    return a

def norm(e,n):
    errarray = [0]*n
    for i in range (0,n):
        errarray[i] = exp[i][1] - f(exp[i][0])
    return errarray

n = int (input ('Input number of experiment points: '))
exp = []

print ('Enter data points in order pairs (x,y): ')

for i in range (0,n):
    exp.append([int(j) for j in input("Enter two values:" ).split()])
    

errarray = norm(exp,n)
print ("Error array")
print (errarray)

    

