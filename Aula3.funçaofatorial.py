# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:48:33 2019

@author: lab
"""

def fatorial(n):
    p=1
    if n!=0:
        for i in range (1,n+1):
            p=p*i
    return p

n=int(input("Digite um numero: "))
p=int(input("Digite ou valor: "))

combi=fatorial(n)/(fatorial(n-p)*fatorial(p))
arranjo=fatorial(n)/fatorial(n-p)
print("olha o arranjo ai {}".format(arranjo))
print("olha a comb ai {}".format(int(combi)))