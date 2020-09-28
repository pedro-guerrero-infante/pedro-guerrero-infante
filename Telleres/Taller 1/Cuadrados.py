from matplotlib import pyplot as plt
import random
import numpy as np

def sumaCuadrados (ns):
    numeros = 0
    resultados = []
    for i in range (0, len(ns)):
        numeros = ns[i]**2
        print("numeros", numeros)
        suma = 0
        for i in range(1, numeros+1):
            suma = suma + i**2
        resultados.append(suma)
        print("resultados: ", resultados)
    return resultados

ns = [2,3,4,5,6,7,8,9, 10,15,20,25,30,35,40,45,50]
cuadrados = sumaCuadrados(ns)

# Grafica.

plt.plot(ns, cuadrados)
plt.title("Orden de convergencia")
plt.xlabel("N")
plt.ylabel("Suma")
plt.legend()
plt.show()

