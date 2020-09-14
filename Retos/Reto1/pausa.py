#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:51:04 2020

@author: yox
"""

import numpy as np
import fractions
import decimal

def pausa(numero):
    
    try:
        priD = 10*entero(numero)
        segD = 10*entero(priD)
        terD = 10*entero(segD)
        cuaD = 10*entero(terD)
        if(int(priD) == int(segD) & int(segD) == int(terD) & int(segD) == int(cuaD)):
            a = int(fractions.Fraction(decimal.Decimal(float(str(int(numero))+str('.') + str(int(priD))*10 + str(int(priD)+1)))).numerator/1000000000000000)
            b = int(fractions.Fraction(decimal.Decimal(float(str(int(numero))+str('.') + str(int(priD))*10 + str(int(priD)+1)))).denominator/1000000000000000)
            return(fractions.Fraction(decimal.Decimal(str(a/b))))
        else: 
            return numero
        
    except:
        real = numero.real
        imag = numero.imag
        
        priD = 10*entero(real)
        segD = 10*entero(priD)
        terD = 10*entero(segD)
        cuaD = 10*entero(terD)
        
        if(int(priD) == int(segD) & int(segD) == int(terD) & int(segD) == int(cuaD)):
            a = int(fractions.Fraction(decimal.Decimal(float(str(int(real))+str('.') + str(int(priD))*10 + str(int(priD)+1)))).numerator/1000000000000000)
            b = int(fractions.Fraction(decimal.Decimal(float(str(int(real))+str('.') + str(int(priD))*10 + str(int(priD)+1)))).denominator/1000000000000000)
            return(fractions.Fraction(decimal.Decimal(str(a/b))), imag)
        else: 
            return numero

            
def entero(numero):
    try:
        entero = int(numero)
        #Borro la parte entera del numero
        return np.float(numero - entero)
    except:
        #print("Error entero")
        return numero

#print(pausa(1.6666666541616+8j))
#print(pausa(1.66666518165))
#print(pausa(0.3333335916519))