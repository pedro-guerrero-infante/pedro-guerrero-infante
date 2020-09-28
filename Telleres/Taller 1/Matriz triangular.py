from matplotlib import pyplot as plt
import random
import numpy as np

def sumaTrianfularSuperior(matrices):
  resultado = []
  for i in range (0,len(matrices)):
    matriz = np.ones((matrices[i], matrices[i]))
    total = 0
    for fila in range (0,matrices[i]):
      for columna in range (fila+1, matrices[i]):
        total = total + matriz[fila][columna]
    resultado.append(total) 
    print("superior:", resultado)
  return resultado

def sumaTrianfularInferior(matrices):
  resultado = []
  for i in range (0,len(matrices)):
    matriz = np.ones((matrices[i], matrices[i]))
    total = 0
    for fila in range (1, matrices[i]):
      for columna in range (0, fila):
        total = total + matriz[fila][columna]
    resultado.append(total) 
    print("inferior: ", resultado)
  return resultado

matrices = [2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,60,70,80,90,100]
superior = sumaTrianfularSuperior(matrices)
inferior = sumaTrianfularInferior(matrices)

print("matrices", matrices)
print("resultado superior", superior)


# Grafica.

plt.plot(matrices, superior)
plt.plot(matrices, inferior)
plt.title("Orden de convergencia")
plt.xlabel("Matriz nxn")
plt.ylabel("Resultados")
plt.show()
