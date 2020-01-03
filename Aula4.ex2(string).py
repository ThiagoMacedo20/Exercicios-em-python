# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:41:33 2019

@author: lab
"""

frase=input("Digite uma frase:")

frase2=frase[::-1]
frase3=frase2.lower()
print(frase3)

if frase.lower() == frase3:
    print("A frase digitada é palidromo")
