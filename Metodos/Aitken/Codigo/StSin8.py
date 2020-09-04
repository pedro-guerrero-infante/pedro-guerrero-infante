import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Funcion a evaluar
def f(x):
    return np.float128(x*np.sin(x)-1)     ## Cambiar el -1

## DECLARACION DE VARIABLES
    
tolerancia = [10**-8, 10**-16, 10**-32]    ## Tolerancias a evualuar
n0 = 10000                          ## Limite de iteraciones
x = np.arange(-1, 2, 0.1)
#x = np.arange(-1, 0.7, 0.1)           ## Intervalo
#x = np.arange(0.8, 2, 0.1)
ans = []                            ## Resultados
ite = []                            ## Lista de iteraciones
err = []                            ## Error de los resultados

## DECLARACION DE FUNCIONES
#Metodo de biseccion utilizado para camparar la eficacia en el numero de operaciones
def metodobiseccion(f, x0, x1, tol):
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

#Metodo de Steffensen que implementa Aitken para acelerar la convergencia
def Steffensen(f,p0,tol):
   
    resultado = [0, 0]
    for i in range(1,n0) :
        p1 = np.float128(p0 + f(p0))
        p2 = np.float128(p1 + f(p1))
        ## Evitar division por cero
        if (p2 - (2*p1) + p0 != 0) & (pow((p2 - p1),2) != 0):
            p = np.float128(p2 - (pow((p2 - p1),2)/(p2 - (2*p1) + p0)))
            
        #si el punto inicial satisface la tolerancia da un resultado y lo retorna
        if abs(p-p0) < tol:
            resultado[0] = p
            resultado[1] = i
            return resultado
        p0 = p

    return resultado

## GRAFICA DE LA FUNCION

y = []

for k in x:
    y.append(f(k))
    
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("x*sin(x)-1")
plt.grid()
plt.show()


## El siguiente ciclo compara los resultados y el error aproximado por cada una de las 3 tolerancias
xx = []
iteraciones = []
bisecIte = []

for j in tolerancia:
    
    cont = 0
    ans.clear()
    ite.clear()
    err.clear()
    xx.clear()
    
    #Se emplea el metodo de Steffensen para evaluar cada punto del intervalo dado
    for k in x:
        
        if(Steffensen(f,k,j)[1] != 0):
            ans.append(Steffensen(f,k,j)[0])
            ite.append(Steffensen(f,k,j)[1])
            xx.append(k)
            if(cont>3):
                temp = abs((ans[cont-2]-ans[cont-1])/ans[cont-2])*100
                if(temp>20):
                    err.append(1)
                else:
                    err.append(temp)
            if(cont<=3):
                err.append(0)
            cont = cont + 1
    
    plt.plot(xx, ans, label = "Resultados")
    plt.plot(xx, err, label = "Error")
    plt.plot(x, y, label = "Funcion")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.legend()
    plt.title("Metodo de Steffensen " + str(j))
    plt.grid()
    plt.show()
    
    #Se extrae la posición en el arreglo de errores para mostrarlo por consola
    p=100
    cont = 0
    for i in err:
        if(p>abs(i)):
            p = cont
        cont = cont + 1
    
    #Resultados metodo de Steffensen
    print("Tolerancia: ", j)
    print("El resultado es: ", ans[p])
    print("La funcion evaluada en el resultado es:", '{0:.32g}'.format(f(ans[p])))
    print("El numero maximo de iteraciones es: ", min(ite))
    
    h = metodobiseccion(f,min(x),max(x),j)
    
    #Resultados metodo de bisección
    print("Resultado con el metodo de biseccion: "+ str(h[0]))
    print("Numero de iteraciones: "+ str(h[1]))
    
    #Cálculo del error entre ambos metodos
    t = (abs(abs(ans[p])-abs(h[0]))/abs(ans[p])) * 100
    print("El error entre ambos metodos es: ", '{0:.2g}'.format(t))
    
    iteraciones.append(min(ite))
    bisecIte.append(h[1])
    
    
#Grafica donde se relaciona las iteraciones en la stres tolerancias para cada uno de los métodos empleados
data = {'Iteraciones Steffensen':iteraciones, 
        'Iteraciones Biseccion':bisecIte,
        'Tolerancias': ["10^-8", "10^-16", "10^-32"]} 
  
  
df = pd.DataFrame(data) 
fig, ax = plt.subplots()
ax = df.plot(kind = 'bar', x = 'Tolerancias', title= 'Comportamiento respecto a la tolerancia xsenx-1', ax = ax)

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    

