library("pracma")
library("ggplot2")
library("Rcpp")

#Funciones
specify_decimal <- function(x, k) trimws(format(round(x, k), nsmall=k))

An <- function(final, Fx){
  
  total <- 0
  ciclo <- seq(0.1, final, 0.1)
  
  for (n in ciclo) {
    x2 <- Fx(n+2)
    x1 <- Fx(n+1)
    x <- Fx(n)
    operacion <- as.double((x2)-((x2-x1)^2)/(x2-(2*x1)+x))
    total <- c(total, operacion)
  }
  
  total
}

Aitken = function(f, p0, tolerance){
  iter = 0
  p1 = 0
  while (TRUE) {
    iter = iter +1
    p1 = f(p0)
    p2 = f(p1)
    if (abs(p1-p0)<tolerance) {
      break
    }
    p0 = p2 - (p2-p1)**2/(p0+p2-2*p1)
  }
  data.frame(p0, iter)
}

Steffensen = function(f, x0, error){
  
  iteraciones = 0
  x1 = 0
  aux = 0
  err = FALSE
  f1 = f(x0)
  
  while(abs(f1) > error && err == FALSE){
    
    iteraciones = iteraciones + 1
    aux = f(x0 + f1) - f1
    
    if(aux == 0){
      
      cat("No se puede calcular la raiz")
      err = TRUE
      
    }else{
      
      x1 = x0-f1*f1/aux
      x0 = x1
      f1 = f(x0)
      
    }
    
  }
  
  if(err == FALSE){
    #cat("Valor aproximado -> ", x1, "Iteraciones ->", iteraciones, "Funcion evaluada: ", specify_decimal(f(x1),15),"\n")
    data.frame(x1, iteraciones)
  }
  
}


#--------------------------------------------
#               TALLER
#--------------------------------------------

xn <- function(n) cos(1/n)

#Grafica de la susesión Xn

plot(xn, 0, 10, col="red" , xlab="Valores para n", ylab="cos(1/n)", main="Susesion Xn") 
grid()
abline(a=0, b=0)



# 1.Verifique el tipo de convergencia en x = 1 independiente del origen

cat("Cunado x = 1:", xn(Inf), "Tipo de convergencia: Absoluta")

#2.Primeros terminos de la susesión

resultado <- An(10, xn)
x <- seq(0.1, 10.1, 0.1)
grafica <- data.frame(x, resultado)
datosF <- 0
for (i in x) {
  datosF <- c(datosF, xn(i))
}
datosF[2] = 1.42

plot(x = x, y = resultado, col="blue", type = "l", main = "Resultados An", asp = 0, xlab = "Valores para n", ylab = "Resultados")
par(new=TRUE)
plot(x = x, y = datosF[-1], type = "l", col="red" , xlab="", ylab="", axes=FALSE)
legend("bottomright", legend = c("Metodo Aitken", "Susesion Xn"),
       fill=c("blue", "red"), cex = 0.8, text.font = 4, bg = "grey")
grid()

ggplot(data = grafica, 
       mapping = aes(x = x, 
                     y = resultado))+
  geom_line()+
  labs(title = "Funcion evaluada")+
  xlab("Valores de x") +
  ylab("F(x)")


#Movimiento de una particula para t>0 con error de 10-16

ft <- function(t) 3*sin(t)^3-1
gt <- function(t) 4*sin(t)*cos(t)

plot(ft,0, 1.5, col="red" , xlab="Tiempo(t)", ylab="f(t), g(t)")
par(new=TRUE)
plot(gt, 0, 1.5, col="blue" , xlab="", ylab="",  axes=FALSE) 
title(main="Coincidencia de graficas")
legend("bottomright", legend = c("f(t)", "g(t)"),
       fill=c("red", "blue"), cex = 0.8, text.font = 4, bg = "grey")
abline(a=0, b=0)
grid()

#FUNCION PARA VER DONDE SE CRUZAN QUE AUN NO SIRVE HPTA
fg <- function(t) -3*sin(t)^3+1+4*sin(t)*cos(t)
particula <- Steffensen(fg, 1, 1e-14)
particula

#--------------------------------------------
#               STEFFENSEN
#--------------------------------------------

fx <- function(x) x^2-cos(x)

print("Con tolerancia 8")
St <- Steffensen(fx, 0, 1e-8)
cat("Metodo de Steffensen: ", St$x1, "Iteraciones: ", St$iter)
Ai <- Aitken(fx, 0, 1e-8)
cat("Metodo de Aitken: ", Ai$p0, "Iteraciones: ", Ai$iter, "Raiz: ", bisect(fx, Ai$p0, Ai$p0*2)$root)
cat("Aitken con la libreria pracma: ", aitken(fx, 0, nmax = 500, tol = 1e-8))

print("Con tolerancia 16")
St <- Steffensen(fx, 0, 1e-15)
cat("Metodo de Steffensen: ", St$x1, "Iteraciones: ", St$iter)
Ai <- Aitken(fx, 0, 1e-16)
cat("Metodo de Aitken: ", Ai$p0, "Iteraciones: ", Ai$iter, "Raiz: ", bisect(fx, Ai$p0, Ai$p0*2)$root)

tol8 <- data.frame(St$iteraciones, Ai$iter)
tol16 <- data.frame(St$iteraciones, Ai$iter)
