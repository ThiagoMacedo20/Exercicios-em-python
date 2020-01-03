# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:45:25 2019

@author: lab
"""
b=int(input('Digite o expo: '))
a=int(input('Digte numero a ser exponenciado: '))
aux=1
for i in range (1,b+1):
    aux*=a
print('\n',aux)