import numpy as np
import math as m
import matplotlib.pyplot as plt

def fx(x):
    return m.log((x+2), np.exp(1))-np.sin(x)

E = 10e-8
ptos = []
ptos.append(-1.9)
ptos.append(-1.1)

n = 1
dif = 100
error = []

while dif > E:
    xn =  (ptos[n]) - ((fx(ptos[n])*(ptos[n]-ptos[n-1]))/(fx(ptos[n])-fx(ptos[n-1])))
    ptos.append(xn)
    dif = np.abs(ptos[n] - ptos[n-1])
    error.append(dif)
    n = n + 1
    
n = 0

while n < len(ptos):
    print(ptos[n]," ",error[n])
    n = n + 1