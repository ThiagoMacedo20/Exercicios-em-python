# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:27:21 2019

@author: lab
"""

frase=input("Digite a frase: ")
for i in range(0,len(frase),2):
    print(frase[i:i +2][::-1],end="")
    