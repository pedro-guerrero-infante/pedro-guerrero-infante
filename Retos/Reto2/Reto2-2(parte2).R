library(pracma)
library(readxl)

#Lectura de los datos 
temperaturas1 = read_excel("/Users/valentinarozobernal/Desktop/Reto2/datos.xls", 
                           sheet = "Itatira")

temperaturas2 = read_excel("/Users/valentinarozobernal/Desktop/Reto2/datos.xls", 
                           sheet = "Santa Quitéria")
#Planeacion de datos Originales
x = seq(from = 1, to = 720, by = 1)
y = temperaturas1$`Temp. Interna (ºC)`

diasIdeales = temperaturas1$`Dia Juliano`

horasIdeales = temperaturas1$Hora

indicesIdeales = x

#Eliminacion del 20% de los datos
ones = rep(1, 720)
eliminate = sample.int(720,720*0.2)
for (e in eliminate) {
  ones[e] = 0
}


newX = c()
newY = c()
i = 1
j = 1

#Validacion de datos adecuados
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


#Graficar 
plot(x,y,type='l', ylab = "Temperaturas", xlab = "Indices Ideales")

lines(spline(newX,newY,n=200),col=2)

interpolado = splinefun(newX,newY)

arregloInterpolados = c()
k = 1

error = c()

for(var in x)
{
  errorY = interpolado(var)
  error = c(error, abs((y[k] - errorY)/y[k]))
  k = k + 1
}

print(error)

arregloDeCalculos = c()

for (i in 1:length(temperaturas2$`Dia Juliano`)) 
{
  
  auxDia = temperaturas2$`Dia Juliano`[i]
  auxHora = temperaturas2$Hora[i]
  
  for(j in 1:720)
  {
    
    if((diasIdeales[j] == auxDia) && (horasIdeales[j] == auxHora))
    {
      arregloDeCalculos = c(arregloDeCalculos,indicesIdeales[j])
    }
  }
}

nuevosY = c()

errorNuevaEstacion = c()

z = 1
for (variable in arregloDeCalculos) 
{
  nuevosY = c(nuevosY, interpolado(variable))
  errorNuevaEstacion = c(errorNuevaEstacion, abs((temperaturas2$`Temp. Interna (ºC)`[z] - nuevosY[z])/temperaturas2$`Temp. Interna (ºC)`[z]))
  z = z + 1
}

plot(arregloDeCalculos,temperaturas2$`Temp. Interna (ºC)`, ylab = "Temperaturas", xlab = "Indices Calculados", type = 'l')

lines(arregloDeCalculos, nuevosY, col = 3)

print(errorNuevaEstacion)

maximo = 0

media = 0

for (error in errorNuevaEstacion) {
  
  if(error > maximo)
    maximo = error
  
  media = media + error
  
}
