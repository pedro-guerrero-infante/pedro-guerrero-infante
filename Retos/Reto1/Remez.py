import numpy as np
import cmath
from random import random
from scipy.signal import remez
from scipy import signal
import matplotlib.pyplot as plt
from math import exp
from math import pi
from numpy.linalg._umath_linalg import solve
import sympy as sp

def ChebyShev (intervaloA,intervaloB,listaNumeros):
    numerosCalculados = []
    for i in range(len(listaNumeros)):
        numerosCalculados.append(1/2*(intervaloA + intervaloB)+ 1/2*(intervaloB-intervaloA)*np.cos((2*i-1)/(2*len(listaNumeros))*pi))
    #end for
    return numerosCalculados
#end def
n = 4
tolerancia = np.longdouble(2e-90)
listaNumeros = [(0.0)]*(n+2)

numerosCalculados = ChebyShev(-2e-8, 2e-8, listaNumeros)
#print(numerosCalculados)

def funcionObjetivo(x):
    return np.e**(np.sin(x)-np.cos(x**2))
#end def

fxCheby = []
cont = 0
while( cont < n+2 ):
    fxCheby.append(funcionObjetivo(numerosCalculados[cont]))
    cont = cont + 1
#end while

matrizEcuaciones = np.zeros((n+2,n+2))
for i in range(n+2):
    matrizEcuaciones[i,0] = 1
    for j in range(1, n):
        matrizEcuaciones[i,j] = numerosCalculados[i]**(j-1)
    #endfor
    if (i%2 == 0):
        matrizEcuaciones[i,n+1] = -tolerancia
    else:
        matrizEcuaciones[i,n+1] = tolerancia
    #endif
#enfor

#print(matrizEcuaciones)
minimax =  np.linalg.lstsq(matrizEcuaciones, fxCheby, None)
#print("Minimax: ",minimax[0])
#print("Minimax: ",minimax[1])
#print("Minimax: ",minimax[2])
#print("Minimax: ",minimax[3])

def polinomio(punto):
    polinomio = 0
    i = 0
    while( i < len(minimax[0])-1 ):
        polinomio = polinomio + (minimax[0][i])*((punto)**i)
        i = i + 1
    #end while
    return polinomio
#enddef


nDatos = 25

salto = (2e-8-(-2e-8))/ nDatos
limiteInicio = -2e-8
errorRelativo = []
errorAbsoluto = []
polinomioFinal = []
#---------------------------------------------------------------
taylorFinal = [(0.0)]*(nDatos)
taylorFinal = ChebyShev(-2e-8, 2e-8, taylorFinal)
Taylor = []
#---------------------------------------------------------------
Remez = []

punto = salto

for i in range (nDatos):
    errorRelativo.append(abs((funcionObjetivo(punto)-polinomio(punto))/funcionObjetivo(punto)))
    errorAbsoluto.append(abs(funcionObjetivo(punto)-polinomio(punto)))
    polinomioFinal.append(polinomio(punto))
    #---------------------------------------------------------------
    Taylor.append(funcionObjetivo(taylorFinal[i]))
    Remez.append(sp.series(funcionObjetivo(punto), punto))

    #---------------------------------------------------------------
    punto = punto + salto
#end for
DiferenciaTaylorRemez = [] 
k = 0
while( k < nDatos ):
    DiferenciaTaylorRemez.append(abs(Taylor[k]-Remez[k]))
    k = k + 1
#end while

print("DiferenciaTaylorRemez ",DiferenciaTaylorRemez)
print("Taylor ",Taylor)
print("Remez ",Remez)


print("relativo ",errorRelativo)
print("absoluto: ",errorAbsoluto)
print ("tam absoluto", len(errorAbsoluto))
print ("tam relativo", len(errorRelativo))

x = np.arange(-2e-8, 2e-8, salto)
plt.plot(x, errorRelativo, label = "Error Relativo")
plt.plot(x, polinomioFinal, label = "Función")
plt.legend()
plt.title("Error relativo de la función e^(sin(x)-cos(x^2)")
plt.xlabel("X")
plt.ylabel("Función evaluada en x")
plt.show()

plt.plot(x, errorAbsoluto, label = "Error Absoluto")
plt.plot(x, polinomioFinal, label = "Función")
plt.legend()
plt.title("Error absoluto de la función e^(sin(x)-cos(x^2)")
plt.xlabel("X")
plt.ylabel("Función evaluada en x")
plt.show()


plt.plot(x, Remez, label = "Algoritmo de Remez")
plt.plot(x, Taylor, label = "Algoritmo de Taylor")
plt.plot(x, DiferenciaTaylorRemez, label = "Diferencia entre aproximaciones")
plt.legend()
plt.title("Taylor vs Remez")
plt.xlabel("X")
plt.ylabel("Funciones evaluadas en x")
plt.show()