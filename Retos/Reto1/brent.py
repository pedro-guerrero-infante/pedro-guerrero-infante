import numpy as np
import matplotlib.pyplot as plt
import pausa
import pandas as pd

def f(x):
    return np.float128(x**3-2*x**2+(4/3)*x-(8/27))


#Ingresa una función, y un intervalo a y b, tol que equivale a la tolerancia
def brent(f, a, b, tol, maxItera):
    c = a
    n = 0
    arr = []
    while (abs(c-b)>tol*(abs(b)+1) or ((n< maxItera) or (f(b)> tol))):
        n = n+1
        x = 0
        if np.complex128((a) * f(b)) < 0:
            a, b, x = secante(f, a, b)
        else:
            if(iteraSecante(a, b, c, f) is True):
                a, b, x = secante(f, a, b)
            else:
                b = b-0.5*(c-b)
                c, b = metodobiseccion(f, c, b)
        if np.complex128(f(a) * f(b)) < np.complex128(0):
            c = a
        arr.append(b)
        
        if(np.complex128(f(b))<tol):
            return (n,b,arr)
        if(type(b)=='complex'):
            if(f(pausa.pausa(b[1]))==0.0):
                return (n,b,arr)
        else:
            if(f(pausa.pausa(b))==0.0 ):
                return (n,b,arr)
        
    return (n,b,arr)
        

#verifica si el resultado está en el otro intervalo
def iteraSecante(a, b, c, f):
    x2 = 0 
    x22 = 0
    x2 = secante (f, a, b)[2]
    x22 = secante (f, c, b)[2]
    if(x2 == x22):
        return True
    else:
        return False
    
#1 iteracion del metodo de la secante
def secante (f, x0, x1):
    x2 = 0 
    if abs(f(x1)) != abs(f(x0)):
        x2 = np.complex128(x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0))))
        x0 = np.complex128(x1)
        x1 = x2
    return (x0, x1, x2)


#1 iteracion del metodo de bisección
def metodobiseccion(f, x0, x1):
    x2 = 0
    x2=np.float128((x0+x1)/2)
    if f(x0)*f(x2)>0: 
        x0=x2
    else:
        x1=x2
    return (x0, x1)

def steffensen(f,p0,tol):
   
    n0 = 10000
    resultado = [0, 0]
    for i in range(1,n0) :
        p1 = p0 + f(p0)
        p2 = p1 + f(p1)
        #print("1:", pow((p2 - p1),2))
        #print("2:",p2 - (2*p1) + p0)
        ## Evitar division por cero
        if (p2 - (2*p1) + p0 != 0) & (pow((p2 - p1),2) != 0):
            p = p2 - (pow((p2 - p1),2)/(p2 - (2*p1) + p0))
        #print("3:",p-p0)
        if abs(p-p0) < tol:
            #print("Converge after %f iterations"%i)
            resultado[0] = p
            resultado[1] = i
            return resultado
        p0 = p
    #print('failed to converge in %f iterations' %n0)
    return resultado

def biseccion(f, x0, x1, tol):
    cont = 0
    while x1-x0>=tol:
        cont = cont + 1
        x2=np.float128((x0+x1)/2)
        if f(x2)==0:
            return (x2, cont)
        else:
            if f(x0)*f(x2)>0: 
                x0=x2
            else:
                x1=x2
    return (x2, cont)


tolerancias = [10**-8, 10**-16, 10**-32]
numeros = []
itera = []
st = []
bis = []
barrasBr = []
barrasSt = []
barrasBi = []

print("PROBLEMA PRINCIPAL")

for i in tolerancias:
    numeros = brent(f, -2, 2, i, 10)[2]
    itera = brent(f, -2, 2, i, 100)
    x = np.arange(-2, 2, 4/len(numeros))
    st = steffensen(f, -2, i)
    bis = biseccion(f, -2, 2, i)
    
    plt.plot(x, numeros)
    plt.title("Método de Brent con " + str(i))
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.show()
    print("Metodo de Brent")
    print("Iteraciones: ",itera[0])
    print("Resulado: ", itera[1])
    print("Resultado expresado en fracción (en caso de ser un decimal periodico): ", pausa.pausa(itera[1]))
    print("Evaluado en f(x): ", f(itera[1]))
    print()
    print("Con el metodo de Steffensen: ")
    print("Resultado: ", st[0])
    print("# de iteraciones: ", st[1])
    print("Error: ", (abs(st[0]-itera[1])/(itera[1]))*100)
    print()
    print("Comparado con el metodo de bisección:")
    print("Resultado: ", bis[0])
    print("# de iteraciones: ", bis[1])
    print("Error: ", (abs(bis[0]-itera[1])/(itera[1]))*100)
    
    barrasBr.append(itera[0])
    barrasSt.append(st[1])
    barrasBi.append(bis[1])
    
    
#Grafica donde se relaciona las iteraciones en la stres tolerancias para cada uno de los métodos empleados
data = {'Iteraciones Brent':barrasBr, 
        'Iteraciones Steffensen':barrasSt,
        'Iteraciones Biseccion':barrasBi,
        'Tolerancias': ["10^-8", "10^-16", "10^-32"]} 
  
  
df = pd.DataFrame(data) 
fig, ax = plt.subplots()
ax = df.plot(kind = 'bar', x = 'Tolerancias', title= 'Comportamiento respecto a la tolerancia', ax = ax)

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    
print()
print("PARA NUMEROS IMAGINARIOS")
print()

def g(x):
    return np.complex128((x*x*x*x)-9*(x*x)-5*(x*x*x)+155*x-250)

numerosC = []
bisC = []

for i in tolerancias:
    
    print(i)
    bisC = brent(g, 3-3j, 5-3j, i, 10000)
    
    print("Resultado: ", bisC[1])
    print("Iteraciones: ", bisC[0])
   
    
    
    
    
    
    
    
    
    
    
