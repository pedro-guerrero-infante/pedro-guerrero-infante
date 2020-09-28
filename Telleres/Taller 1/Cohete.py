## SI FUNCIONA!
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.longdouble(6+(2.13*(x**2))-(0.0013*(x**4)))

## DECLARACION DE VARIABLES
    
tolerancia = [10**-8, 10**-16, 10**-32]    ## Tolerancias a evualuar
n0 = 10000                          ## Limite de iteraciones
x = np.arange(0, 42, 1)
#x = np.arange(-1, 0.7, 0.1)           ## Intervalo
#x = np.arange(0.8, 2, 0.1)
ans = []                            ## Resultados
ite = []                            ## Lista de iteraciones
err = []                            ## Error de los resultados

## DECLARACION DE FUNCIONES

def metodobiseccion(f, x0, x1, tol):
    cont = 0
    while x1-x0>=tol:
        cont = cont + 1
        x2=np.longdouble((x0+x1)/2)
        if f(x2)==0:
            return (x2, cont)
        else:
            if f(x0)*f(x2)>0: 
                x0=x2
            else:
                x1=x2
    return (x2, cont)

def Steffensen(f,p0,tol):
   
    resultado = [0, 0]
    for i in range(1,n0):
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

## GRAFICA DE LA FUNCION

y = []

for k in x:
    y.append(f(k))
    
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("6 + (2.13 x t^2)-(0.0013 x t^4)")
plt.grid()
plt.show()

xaux = 1
hmax = 0
while xaux < len(y):
    if( y[xaux-1] > y[xaux] ):
        hmax = y[xaux-1]
        break
    xaux = xaux + 1
## PARA LA PRIMERA TOLERANCIA 10**-8
xx = []
for j in tolerancia:
    
    cont = 0
    ans.clear()
    ite.clear()
    err.clear()
    xx.clear()
    
    for k in x:
        if(Steffensen(f,k,j)[1] != 0):
            ans.append(Steffensen(f,k,j)[0])
            ite.append(Steffensen(f,k,j)[1])
            xx.append(k)
            if(cont>3):
                temp = abs((ans[cont-1]-ans[cont])/ans[cont-1])*100
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
    plt.title("Metodo de Steffensen")
    plt.grid()
    plt.show()
    
    p=100
    cont = 0
    for i in err:
        if( p > abs(i) ):
            p = cont
        cont = cont + 1
    
    print("Tolerancia: ", j)
    print("El resultado es: ", ans[p])
    print("La funcion evaluada en el resultado es:", f(ans[p]))
    print("El numero maximo de iteraciones es: ", min(ite))
    
    h = metodobiseccion(f,min(x),max(x),j)
    
    print("Resultado con el metodo de biseccion: "+ str(h[0]))
    print("Numero de iteraciones: "+ str(h[1]))
    print("hmax: ",hmax," metros de altura.")  