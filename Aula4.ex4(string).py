# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:54:47 2019

@author: lab
"""

frase=input("Digite uma frase: ")
caractere=input("Digite um caractere: ")
q=0
for letra in frase:
    if letra in caractere:
        print(letra)
        q+=1
print(q)
