# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:47:58 2019

@author: lab
"""
frase=input("Digite uma frase:")
vogais="aeiou"
q=0
for letra in frase:
    if letra in vogais:
        print(letra)
        q+=1
        
print("\n",q)
