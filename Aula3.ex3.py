# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:46:12 2019

@author: lab
"""

def ordem(n,y):
    lista=[]
    if n>y:
        n,y=y,n
    for i in range(n+1,y):
        lista.append(i)
    return lista
n=10
y=20
print(ordem(n,y))
