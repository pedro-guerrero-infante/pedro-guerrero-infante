#Taller 1 punto 1
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import struct
from math import sqrt
import sys

#Punto 1- Número de operaciones
#1.1

#Polinomio de grado 50 evaluado en x igual que su derivada
def evaluarHorner(x, grado):
    resultado = 0
    der = 0
    cont = 0
    for i in range(0, grado+1):
        if( i == 0):
            resultado += 1
        else:
            if(i == 1):
               der += 1 
            else:
                temp = 1*i+1
                der += temp*x**i-1
            resultado += x**i
            cont = cont +1
            
    return resultado, der, 


#Evaluar la ecuacion equivaente y su derivada
def q(x):
    c = x
    #res = ((x**51)-1)/(x-1)
    x = sp.Symbol('x')
    f = ((x**51)-1)/(x-1)
    g = ((50*x**51)-(51*x**50)+1)/((x-1)**2)
    value = {x: c}
    f.evalf(subs = value)
    g.evalf(subs = value)
    der = sp.N(g, subs=value)
    res = sp.N(f, subs=value)
    return res, der

    

#1.2 Números binarios
#Esta función convierte de binario a decimal
def binarioDecimal(binario):
    #Se convierte a string para saber cuantos dígitos tiene el numero ingresado
    binario = str(binario)
    decimalEntero = 0
    decimalComa = 0 
    decimal = ""
    binarioDecimal = ""
    binarioEntero = ""
    bandera = False
        
    #Se separa la parte entera de la parte decimal
    for i in binario:   
        if bandera == True:
            binarioDecimal += i
            
        if i == ".":
            bandera = True
        
        if bandera == False:
            binarioEntero += i
            
    
    #Para operar la parte entera
    exp = len (binarioEntero) -1
    #se recorre el número
    for i in binarioEntero:
        #se aplica la formula para convertir
        decimalEntero += (int(i) * 2**(exp))
        exp = exp - 1
    
    #Se opera la parte decimal
    exp = 1
    fijo = 0.5
    for i in binarioDecimal:
        decimalComa += (int(i) * (exp*fijo))
        exp = exp * fijo
    
    decimal = decimalEntero + decimalComa
    
    return decimal


#Esta función convierte de decimal a binario
def decimalBinario(decimal):
    binarioComa = ""
    binarioEntero = ""
    
    decEntero = ""
    decComa = ""
    decimal = str(decimal)
    bandera = False
    
    for i in decimal:
        if i == ".":
            bandera = True
            
        if bandera  == False:
            decEntero += i
            
        if bandera == True:
            decComa += i
    
    decComa = float(decComa)
    decEntero = int(decEntero)
    
   
    #Se opera la parte entera
    while decEntero // 2 != 0:
        binarioEntero = str(decEntero % 2) + binarioEntero
        decEntero = decEntero // 2
    
    #Se opera la parte decimal teniendo en cuenta la periodicidad
    ban = True
    grupo = 0
    cont = 0
    temp = ""
    ant = "0"
    num = 0
    while ban == True:
        grupo = 0
        bic = ""
        while grupo < 4 and ban == True:
            bina = decComa * 2
            bina = str(bina)
            bi = bina.split(".")
            binarioComa += bi[0]
            bic += bi[0]
            if(float(bi[1]) == 0.0):
                ban = False
            else:
                y = "." + str(bi[1])
                decComa = float(y)
            grupo = grupo + 1
        if cont != 0:
            ant = temp
        cont = cont + 1
        temp = bic
        if(temp == ant):
            num = num +1
        #Despues de cuatro veces que repita los mismos cuatro bits para y se toma como periódico
        if(num>=3):
            ban = False
        
    
    return str(decEntero) + binarioEntero + "." + binarioComa

#Ejercicios parte 3

#Punto 3
#La presición doble se define con 64 bits
def float_IEEE64Bits(valor):
    #Se accede a la librería strict con el fin de manipular números binarios
    bits, = struct.unpack('Q', struct.pack('d', valor))
    return "{:064b}".format(bits)


#Punto 8
#Convertir de decimal a hexadecimal
def aHexadecimal(decimal):
    hexadecimalEntero = ""
    hexadecimalDecimal = ""
    
    decEntero = ""
    decDec = ""
    
    hexas = "0123456789ABCDEF"
    decimal = str(decimal)
    bandera = False
    
    for i in decimal:
        if i == ".":
            bandera = True
        
        if bandera == True:
            decDec += i
            
        if bandera == False:
            decEntero += i
            
    decDec = float(decDec)
    decEntero = float(decEntero)
    
    #operar parte entera
    while decEntero != 0.0:
        residuo = decEntero % 16
        hexadecimalEntero += str(hexas[int(residuo)])
        decEntero = int(decEntero/16)
            
    #operar parte decimal
    ban = True
    grupo = 0
    cont = 0
    temp = ""
    ant = "0"
    num = 0
    while ban == True:
        grupo = 0
        bic = ""
        while grupo < 2 and ban == True:
            res = str(decDec * 16)
            r = res.split(".")
            hexadecimalDecimal += hexas[int(r[0])]
            he = "." + r[1]
            if(float(he) == 0.0):
                ban = False
            decDec = float(he)
            grupo = grupo + 1
        if cont != 0:
            ant = temp
        cont = cont + 1
        temp = bic
        if(temp == ant):
            num = num +1
        if(num>=3):
            ban = False
        
    return hexadecimalEntero + "." + hexadecimalDecimal
    

#Punto 7
def cuadratica(a, b, c): 
    x1 = 0
    x2 = 0
    if a != 0:
        x1 = np.float128((-b + sqrt(b**2 - 4*a*c)) / (2 * a))
        x2 = np.float128((-b - sqrt(b**2 - 4*a*c)) / (2 * a))
        return(x1, x2)
    else:
        if b != 0:
           x = np.float128(-c / b)
           return x
        else:
           if c != 0:
              print ('La ecuacion no tiene solucion. ')
     
           else:
              print ('La ecuacion tiene infinitas soluciones. ')
    


print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
print("\nNúmero de operciones")
print("Evaluar P(x) en x = 1.00000000001: ", evaluarHorner(1.00000000001, 50)[0])
print("Evaluar derivada de P(x): ", evaluarHorner(1.00000000001, 50)[1])
print("Evaluar x =  1.00000000001 en su expresión equivalente Q(x): ", q(1.00000000001)[0])
print("Evaluar derivada de Q(x): ", q(1.00000000001)[1])
print("Error entre el resultado de P(x) y Q(x): ", (abs(q(1.00000000001)[0]-evaluarHorner(1.00000000001, 50)[0])/q(1.00000000001)[0]) *100)
print("Error entre el resultado de las derivadas de P(x) y Q(x): ", (abs(q(1.00000000001)[1]-evaluarHorner(1.00000000001, 50)[1])/q(1.00000000001)[1]) *100)

Polinomio = []
Equivalente = []
PolDerivada = []
EquivDerivada = []
error = []
errorDer = []
cont = 0

x = np.arange(-5, 5, 0.01)
for i in x:
    pol = evaluarHorner(i, 50)
    eq = q(i)
    
    Polinomio.append(pol[0])
    PolDerivada.append(pol[1])
    Equivalente.append(eq[0])
    EquivDerivada.append(eq[1])
    error.append((abs(eq[0]-pol[0])/eq[0]))
    errorDer.append((abs(eq[1]-pol[1])/eq[1])*100)
    
plt.figure(0)
plt.plot(x, Polinomio, label = "Polinomio")
plt.plot(x, error, label = "Error")
plt.plot(x, Equivalente, label = "Equivalente")
plt.title("Error de cálculo entre P(x) y Q(x)")
plt.ylim(-1, 6)
plt.xlim(-0.75, 1)
plt.legend()
plt.show


plt.figure(1)
plt.plot(x, PolDerivada, label = "Polinomio Derivada")
plt.plot(x, errorDer, label = "Error Derivada")
plt.plot(x, EquivDerivada, label = "Equivalente Derivada")
plt.title("Error de cálculo entre las derivadas de P(x) y Q(x)")
plt.legend()
plt.show


print("\nNumeros binarios")
print ("\n15 bits primeros bits de pi")
print("Base 10: PI  \tBinario: ", decimalBinario(3.141592653589793)[:16])


print("\nConvertir de binario a base 10")
print("Binario: 1010101  \t\tBase 10: ", binarioDecimal(1010101))
print("Binario: 1011.101  \t\tBase 10: ", binarioDecimal(1011.101))
print("Binario: 10111.010101  \tBase 10: ", binarioDecimal(10111.010101))
print("Binario: 111.1111  \t\tBase 10: ", binarioDecimal(111.1111))


print("\nConvertir de base 10 a binario")
print("Base 10: 11.25  \tBinario: ", decimalBinario(11.25))
print("Base 10: 2/3  \tBinario: ", decimalBinario(2/3))
print("Base 10: 30.6  \tBinario: ", decimalBinario(30.6))
print("Base 10: 99.9  \tBinario: ", decimalBinario(99.9))

print("\n-------------------------------------------------------------")
print("\nEjercicios")
#3
print("\n3. Precisión doble IEEE")
num = str(float_IEEE64Bits(0.4))
print("Número de punto flotante para 0.4: ", num)
print("Signo: " , num[:1])
print("Exponente: ", num[1:12])
print("Mantisa: ", num[12:64])
fl = 0.4*(1+sys.float_info.epsilon)
print("En notación decimal: ", fl)

#4
print("\n4. Error de redondeo")
print("x=0.4 \tError de redondeo: ", abs(0.4-fl))
#6
print("\n6. Real a hexadecimal")
print("Real: 9.4 \tHexadecimal: ", aHexadecimal(9.4))

#7
print("\n7. Calcular raíces de x^2 + 9^12 = 3")
val = cuadratica(1, 9**12, -3)
print("x1 =", val[0], "\tx2 =", val[1])

#Punto 8
#x^2+bx-10^-12=0
print("\n8. Calcular raíces de x^2 + bx - 10^-12 = 0")
n = np.float128(cuadratica(1, 101, 10**-12))

print("Con b= 101, x1 = ", n[0], "\tx2 = ", n[1])
print("En presición doble bits: x1=", float_IEEE64Bits(n[0]))
print("En presición doble bits: x2=", float_IEEE64Bits(n[1]))

print("\n-------------------------------------------------------------")
print("-------------------------------------------------------------")
























