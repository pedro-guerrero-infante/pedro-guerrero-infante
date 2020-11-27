xParalelo <- c(1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018)	

yParalelo <- c(4225649,4360948,4502390,4648463,4797534,4947890,
                      5105935,5261692,5413484,5559851,5699655,5828528,
                      5952563,6072489,6189030,6302881,6412400,6520473,
                      6627568,6734041,6840116,6945216,7050228,7155052,
                      7259597,7363782,7467804,7571345,7674366,7776845,7878783,7980001,8080734,8181047)

malthus<-function(t, k, p0)
{
  return(p0*exp(k*t))
}

Adams_Bashforth <- function(xParalelo,yParalelo)
{
  respuesta_x <- c()
  respuesta_y <- c()
  
  x0 <- 1
  y0 <- yParalelo[1]
  xf <- 20
  numPasos <- 20
  h <- 1
  x_ant <- x0
  y_ant <- y0
  x_act <- x_ant + h
  t <- 1
  k <- 5
  p0 <- yParalelo[1]
  y_act <- y_ant + h + malthus( t, k, p0 )
  
  respuesta_x[1] <- x0
  respuesta_y[1] <- y0 
  respuesta_x[2] <- x_act
  respuesta_y[2] <- y_act
  
  x_sig <- 0
  y_sig <- 0
  malthus_ant <- 0
  malthus_act <- 0
  i <- 3
  while(  i <= numPasos )
  {
    malthus_ant <- malthus( x_ant, k, y_ant )
    malthus_act <- malthus( x_act, k, y_act )

    x_sig <- x_act + h
    y_sig <- y_act + (h/2) *(( (3*malthus_act) - malthus_ant))
    
    respuesta_x[i] <- x_sig
    respuesta_y[i] <- y_sig
    
    x_ant <- x_act
    y_ant <- y_act
    x_act <- x_sig
    y_act <- y_sig 
    
    i <- i + 1
  }
  
  cat("rest x: ",respuesta_x)
  cat("rest y: ",respuesta_y)
  
  plot(respuesta_x,respuesta_y,xlab="tiempo (Nº años)",ylab="poblacion",main="Crecimiento de poblacion Modelo de Adams",type="l", col="black")
  lines( respuesta_x, respuesta_y, col = "red")
  legend("topleft", legend = c("Exactos", "Simulación"), col= 2:1, pch=1)
}


Adams_Bashforth(xParalelo, yParalelo)


