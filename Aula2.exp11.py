# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:43:05 2019

@author: lab
"""

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        print(a)
        
print(fibonacci(10))        
 