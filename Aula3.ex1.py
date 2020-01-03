# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:23:00 2019

@author: lab
"""

import random

def parimpar(n):
    return n %2==0
       

for i in range (50):
    n=random.randint(25,92)
    if parimpar(n):
        print('O numero {} é par'.format(n))
    else:
        print('O numero {} é impar'.format(n))