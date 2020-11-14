library(pracma)
library(readxl)

#Lectura de los datos 
temperaturas1 = read_excel("/Users/valentinarozobernal/Desktop/Reto2/datos.xls", 
                           sheet = "Itatira")

#Presentación de datos originales
x = seq(1,length(temperaturas1$`Temp. Interna (ºC)`),1)
y = temperaturas1$`Temp. Interna (ºC)`

plot(x,y, type = "line", main = "Datos iniciales", ylab = "Temperaturas", xlab = "Indices Ideales")

#Eliminar 20% y rellenar datos

set.seed(0)

ones = rep(1, 720)
eliminate = sample.int(720,720*0.2)
for (e in eliminate) {
  ones[e] = 0
}


newX = c()
newY = c()

i = 1
j = 1

for (o in ones)
{
  if(o == 1)
  {
    newX[i] = x[j]
    newY[i] = y[j]
    i = i + 1
  }
  j = j +1
}


##Ajuste y nuevas graficas 

#spline
ajuste1 = spline(newX, newY)
funAjuste1 = splinefun(newX, newY)

plot(x,y, type = "line", main = "Comparación spline", ylab = "Temperaturas", xlab = "Indices Ideales")
lines(ajuste1, col = "red")


#interpolación lineal
ajuste2 = approx(newX, newY, method = "linear", n = length(newX))
funAjuste2 = approxfun(newX, newY)

plot(x,y, type = "line", main = "Comparación approx", ylab = "Temperaturas", xlab = "Indices Ideales")
lines(ajuste2, col = "blue")

plot(x,y, type = "line", main = "Comparación con ambos metodos", ylab = "Temperaturas", xlab = "Indices Ideales")
lines(ajuste1, col = "red")
lines(ajuste2, col = "blue")

## Errores respectivos y combinación de metodos

errorSpline = c()
errorInter = c()
errorComb = c()

comb = c()

k = 1

for(var in x)
{
  comb[k] = (funAjuste1(var) + funAjuste2(var))/2
  
  errorSpline[k] = round(abs((y[k] - funAjuste1(var))/y[k]),2)
  errorInter[k] = round(abs((y[k] - funAjuste2(var))/y[k]),2)
  errorComb[k] = round(abs(abs((y[k] - comb[k])/y[k])),2)
  
  k = k + 1
}

plot(x,y, type = "line", main = "Comparación combinada", ylab = "Temperaturas", xlab = "Indices Ideales")
lines(x, comb, col = "purple")


#print(errorSpline)
#print(errorInter)
#print(errorComb)


cat("VALIDACIÓN CRUZADA")

cat("Con el uso de la funcion spline")
cat("Cantidad de errores: ", sum(errorSpline != 0))
cat("Error maximo: ", max(errorSpline))
cat("Error minimo: (para valores distintos de cero)", min(errorSpline[errorSpline>0]))
cat("Error medio: (para valores distintos de cero)", median(errorSpline[errorSpline>0]))
cat("Indice de Jaccard: ", round(sum(errorSpline == 0)/ length(x), 4))

errorInter[1] = 0
cat("Con el uso de la funcion approx")
cat("Cantidad de errores: ", sum(errorInter != 0))
cat("Error maximo: ", max(errorInter))
cat("Error minimo: (para valores distintos de cero)", min(errorInter[errorInter>0]))
cat("Error medio: (para valores distintos de cero)", median(errorInter[errorInter>0]))
cat("Indice de Jaccard: ", round(sum(errorInter == 0)/ length(x), 4))

errorComb[1] = 0
cat("Con el uso combinado")
cat("Cantidad de errores: ", sum(errorComb != 0))
cat("Error maximo: ", max(errorComb))
cat("Error minimo: (para valores distintos de cero)", min(errorComb[errorComb>0]))
cat("Error medio: (para valores distintos de cero)", median(errorComb[errorComb>0]))
cat("Indice de Jaccard: ", round(sum(errorComb == 0)/ length(x), 4))