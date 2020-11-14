#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans

coordenadas = pd.read_csv("coordenadas.csv")
print(coordenadas)

#Visualizar la ubicación de las diferentes estaciones
nombres = []
for i in coordenadas.iloc[:,2]:
    nombres.append(i)

print("\n" , nombres, "\n")

fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

cont = 0
for x, y in zip(coordenadas.iloc[:,0], coordenadas.iloc[:,1]):
    plt.plot((x,), (y,), 'go')
    plt.text(x, y, nombres[cont])
    cont = cont + 1
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Estaciones")
plt.savefig("Coordenadas.pdf")

#Encontrar la estación más cercana a Santa Quiteria
y1 = 0
x1 = 0
for i in range(0, len(coordenadas)):
    if(coordenadas.iloc[i,2]== "Santa Quiteria"):
        x1 = coordenadas.iloc[i,0]
        y1 = coordenadas.iloc[i,1]

a = np.array([x1,y1])
distancias = []
for i in range(0, len(coordenadas)):
    if(coordenadas.iloc[i,2]!= "Santa Quiteria"):
        x2 = coordenadas.iloc[i,0]
        y2 = coordenadas.iloc[i,1]
        b = ([x2, y2])
        distancias.append((coordenadas.iloc[i,2], np.sqrt(np.sum(np.power(b-a, 2)))))
        
print(distancias)

menor = distancias[0][1]
ciudad = ""
for i in range(1, len(distancias)):
    if distancias[i][1]<menor:
        menor = distancias[i][1]
        ciudad = distancias[i][0]
        
print("\nLa estacion mas cercana a Santa Quiteria es: " + ciudad)

        












    

