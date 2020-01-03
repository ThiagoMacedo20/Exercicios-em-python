# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:23:08 2019

@author: lab
"""

m=int(input('Digite a quantidade do inicio: '))
n=int(input('Digite ate quando vai : '))


soma=0
if m>n:
    m,n=n,m
    
for i in range (m,n):
    if i %2==0:
       print(i,end='-')
       soma+=i

print('\n',soma)
        