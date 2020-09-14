from numpy import array, exp, real, imag, empty, finfo
import numpy as np
import cmath
import pandas as pd
import matplotlib.pyplot as plt



"""
Si se quiere un coeficiente complejo se escibe de la siguiente manera:
c = 4 +3j, tomando j como la parte imaginaria del número, luego se reemplaza en
la ecuación y el programa calcula el resultado teniendo en cuenta los números
complejos
"""

#Metodo de newton para obtener las raices a evaluar
def newtonRaphson(x0,e,N, coeficientes):
    step = 1
    flag = 1
    condition = True
    cont = 0
    while condition:
        if  hornerPlus(x0, coeficientes, 1)[0] == 0.0:
            print('Error!')
            break
        #Aplica la fórmula
        x1 = np.complex128(x0 - hornerPlus(x0, coeficientes, 0)[0]/hornerPlus(x0, coeficientes, 1)[0])
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(hornerPlus(x0, coeficientes, 0)[0]) > e
        cont = cont + 1
    
    if flag!=1:
        print('No converge.')
    
    return x1, cont

#El método de Horner que deriva y evalua de foemaa eficiente
def hornerPlus(x, coeficientes, N):
    cont = 0
    derivada = []
    SegundaDerivada= []
    grado = len(coeficientes)-1
    
    #Se evalua la primera derivada
    for i in range(0, grado):
        derivada.append(coeficientes[i] * (grado-i))
      
    #Se evalua la segunda derivada
    for i in range(0, grado-1):
         SegundaDerivada.append(derivada[i] * ((grado-1)-i))
    
    if N == 0:
        resultado = coeficientes[0]
        for i in range(1, len(coeficientes)): 
            resultado = np.complex128(coeficientes[i] + x * resultado)
            cont = cont +1
        return (resultado, cont, x)
    
    elif N == 1:            
        resultado = derivada[0]
        for i in range(1, len(derivada)): 
            resultado = np.complex128(derivada[i] + x * resultado)
            cont = cont +1
        return (resultado, cont, x)
    
    elif N == 2:            
        resultado = SegundaDerivada[0]
        for i in range(1, len(SegundaDerivada)): 
            resultado = np.complex128(SegundaDerivada[i] + x * resultado)
            cont = cont +1
        return (resultado, cont, x)
        
    
    
#Donde se ejecuta todo el algortitmo
def principal(coeficientes):
    """Función que evalua el algoritmo de Horner y devuelve el resultado y el
    número de multiplicaciones realizadas"""
    grado = len(coeficientes)-1
    arrX = [-9, 1, 3-7j, 3+7j]
    Raiz = 0
    Contador = 0
    tolerancias = [10**-8, 10**-12, 10**-24]
    it = []
    itlAG= []
    itB = []
    raices = []

     #Evalua el polinomio y las derivadas en un punto dado
    print("Polinomio: ",coeficientes)
    print("Evaluado en 2: ", hornerPlus(2, coeficientes, 0)[0])
    print("Primera dervivada evaluada en 2: ", hornerPlus(2, coeficientes, 1)[0])
    print("Segunda derivada evaluada en 2: ", hornerPlus(2, coeficientes, 2)[0])    

    #Compara eficiencia en tres tolerancias en el método de Laguerre y Newton
    for c in tolerancias:
        it.clear()
        itlAG.clear()
        itB.clear()
        print("")
        print("\nRaices de Newton con tolerancia " + str(c))    
        for m in arrX:
            Raiz, Contador = newtonRaphson(m,c,100, coeficientes)
            rai, con = metodobiseccion(coeficientes, m, 5,c)
            itB.append(con)
            it.append(Contador)
            print ("Raiz: ", Raiz)
            print ("Iteraciones: ", Contador)
            
            
        
        print("")  
        print("\nRaices de Laguerre con tolerancia " + str(c)) 
        itLAG, raices = Laguerre(arrX, grado, coeficientes,c)
        
        data = {'Iteraciones Newton':it, 
        'Iteraciones Laguerre':itLAG,
        'Raices': raices} 
        
        #Se grafica la solución
        df = pd.DataFrame(data) 
        fig, ax = plt.subplots()
        ax = df.plot(kind = 'bar', x = 'Raices',  title= 'Numero de iteraciones con tol = ' + str(c) , ax = ax)
        
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    
        print("\nBisección con tolerancia " + str(c))
        print("Raiz: ", rai)
        print("Iteraciones: ", con)
        
        #Compara con bisección
        if(c == 10**-24):
            data = {'Iteraciones Newton':it, 
            'Iteraciones Laguerre':itLAG,
            'Iteraciones Bisección':itB,
            'Raices': raices} 
            
            #Se grafica la solución
            df = pd.DataFrame(data) 
            fig, ax = plt.subplots()
            ax = df.plot(kind = 'bar', x = 'Raices',  title= 'Numero de iteraciones con tol = ' + str(c) , ax = ax)
            
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        
            


#Método de Laguerre para encontrar las raices dado un polinomio
def Laguerre(arrX, grado, coeficientes, epsilon):
    it = []
    ra = []
    for k in arrX:
        iteraciones = 0
        n = grado
        start = k
        start = complex(start)
        while True:
            px = hornerPlus(start, coeficientes, 0)[0]
            if not px:
                if(start.imag) == 0:
                    start = start.real
                    print ("Resultado: ", start)
                    print ("Iteraciones: ", iteraciones)
                    it.append(iteraciones)
                    ra.append(round(start))
                else:
                    print ("Resultado: ", start)
                    print ("Iteraciones: ", iteraciones)
                    it.append(iteraciones)
                    if(start.imag >0):
                        ta = str(round(start.real))+ " +"+ str(round(start.imag))+"j"
                        ra.append(ta)
                    else:
                        ta = str(round(start.real))+ " "+ str(round(start.imag))+"j"
                        ra.append(ta)
       
               
                break
            g = hornerPlus(start, coeficientes, 1)[0]/ px
            h = g ** 2 - hornerPlus(start, coeficientes, 2)[0] / px
            dp = np.complex128(cmath.sqrt((n - 1) * (n * h - g**2)))
            d1 = g + dp
            d2 = g - dp
            if abs(d2) > abs(d1):
                d = d2
            else:
                d = d1
            a = n / d
            x_n = start - a
            iteraciones = iteraciones + 1
            if str(start) == str(x_n) or abs(start - x_n) < epsilon:
                if(start.imag) == 0:
                    start = start.real
                    print("Resultado: ", start)
                    print ("Iteraciones: ", iteraciones)
                    it.append(iteraciones)
                    ra.append(round(start))
                else:
                    print ("Resultado: ", start)
                    print ("Iteraciones: ", iteraciones)
                    it.append(iteraciones)
                    if(start.imag >0):
                        ta = str(round(start.real))+ " +"+ str(round(start.imag))+"j"
                        ra.append(ta)
                    else:
                        ta = str(round(start.real))+ " "+ str(round(start.imag))+"j"
                        ra.append(ta)
                
                break
            start = x_n
    return it, ra


#Método de biseccion utilizado para comparar eficiencia
def metodobiseccion(coeficientes, x0, x1, tol):
    cont = 0
    while x1.real-x0.real>=tol:
        cont = cont + 1
        x2=np.complex128((x0+x1)/2)
        if hornerPlus(x2, coeficientes, 0)[0].real==0:
            return (x2, cont)
        else:
            if hornerPlus(x0, coeficientes, 0)[0].real*hornerPlus(x2, coeficientes, 0)[0].real>0: 
                x0=x2
            else:
                x1=x2
    return (x2, cont)

#Polinomio a evaluar
coeficientes = [1, -5, -9, 155, -250]

#Se prueba con otro polinomio, para ver se puede quitar el compentario y ejecutar
#cof =[1+2j, -2+1j, 9]
#principal(cof)
principal(coeficientes) 




