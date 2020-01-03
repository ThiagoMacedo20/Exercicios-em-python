# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:32:10 2019

@author: lab
"""
a=1
s=0
for i in range (52):
    s+=1/(a**3)
    a+=2
    
p=(s*32)**(1/3)
print(p)