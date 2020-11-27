library(readxl)
library(shiny)
library(Rmpfr)
library(ggplot2)
library(gridExtra)


options(digits= 22)
## Lectura de archivos
nacional = read_excel("AN/reto/Poblaciones.xlsx", 
                      sheet = "Nacional ")
bogota = read_excel("AN/reto/Poblaciones.xlsx", 
                      sheet = "Bogota")
antioquia = read_excel("AN/reto/Poblaciones.xlsx", 
                      sheet = "Antioquia")

# Define UI for application that draws a histogram
if (interactive()) {
  
  ui <- fluidPage(
    
    # Application title
    titlePanel("Crecimiento poblacional"),
    
    # Sidebar with a slider input for number of bins 
    sidebarLayout(
      sidebarPanel(
        radioButtons("Modelo",
                     "Modelo de crecimiento:",
                     choices=list("Modelo de Malthus"=1,"Modelo logistico"=2),
                     selected=1),
        radioButtons("M",
                     "Municipio:",
                     choices=list("Nacional"=1,"Bogotá¡"=2,"Antioquia"=3),
                     selected=1),
        radioButtons("G",
                     "GÃ©nero:",
                     choices=list("Todos"=1,"Femenino"=2, "Masculino"=3),
                     selected=1),
        sliderInput("Carga",
                    "Capacidad de carga (Solo logistico):",
                    min = 5000000,
                    max = 120000000,
                    value = 5000000,
                    step=1),
        sliderInput("T0",
                    "Año inicial:",
                    min = 1985,
                    max = 2010,
                    value = 1985,
                    step=1),
        sliderInput("Tf",
                    "Año final:",
                    min = 1990,
                    max = 2018,
                    value = 1990,
                    step=1),
        actionButton("graf", "Graficar")
      ),
      # Show a plot of the generated distribution
      mainPanel(
        
        plotOutput("distPlot"),
        textOutput("Total")
      )
    )
  )
  
  server <- function(input, output, session) {
    observe({
      v <- reactiveValues(doPlot = FALSE)
      
      observeEvent(input$graf, {
        # 0 will be coerced to FALSE
        # 1+ will be coerced to TRUE
        v$doPlot <- input$graf
      })
     
      output$distPlot <- renderPlot({
        if(v$doPlot==FALSE) return()
        pf = 0
        p5 = 0
        p0 = 0
        poblacion = c()
        if(input$M==1){
          if(input$G==1){
            poblacion = nacional$`Total`
            cont = 1
            years = nacional$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==2){
            poblacion = nacional$`Mujeres`
            cont = 1
            years = nacional$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==3){
            poblacion = nacional$`Hombre`
            cont = 1
            years = nacional$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
        }
        
        if(input$M==2){
          if(input$G==1){
            poblacion = bogota$`Total`
            cont = 1
            years = bogota$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          
          if(input$G==2){
            poblacion = bogota$`Mujeres`
            cont = 1
            years = bogota$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==3){
            poblacion = bogota$`Hombre`
            cont = 1
            years = bogota$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
        }
        
        if(input$M==3){
          if(input$G==1){
            poblacion = antioquia$`Total`
            cont = 1
            years = antioquia$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==2){
            poblacion = antioquia$`Mujeres`
            cont = 1
            years = antioquia$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==3){
            poblacion = antioquia$`Hombre`
            cont = 1
            years = antioquia$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
        }
        
        Graficar(input$T0,input$Tf,p0,pf,p5, input$Modelo, input$Carga, poblacion)
      })
      
      
      output$Total<-renderText({
        if(v$doPlot==FALSE) return()
        pf = 0
        p5 = 0
        p0 = 0
        palabra = ""
        if(input$M==1){
          palabra = "Colombia"
          if(input$G==1){
            poblacion = nacional$`Total`
            cont = 1
            years = nacional$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==2){
            poblacion = nacional$`Mujeres`
            cont = 1
            years = nacional$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==3){
            poblacion = nacional$`Hombre`
            cont = 1
            years = nacional$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
        }
        
        if(input$M==2){
          palabra = "Bogotá¡"
          if(input$G==1){
            poblacion = bogota$`Total`
            cont = 1
            years = bogota$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          
          if(input$G==2){
            poblacion = bogota$`Mujeres`
            cont = 1
            years = bogota$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==3){
            poblacion = bogota$`Hombre`
            cont = 1
            years = bogota$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
        }
        
        if(input$M==3){
          palabra = "Antioquia"
          if(input$G==1){
            poblacion = antioquia$`Total`
            cont = 1
            years = antioquia$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==2){
            poblacion = antioquia$`Mujeres`
            cont = 1
            years = antioquia$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
          if(input$G==3){
            poblacion = antioquia$`Hombre`
            cont = 1
            years = antioquia$`Año`
            for (i in years){
              if(i == input$T0){
                p0 = poblacion[cont]
              }
              if(i == input$Tf){
                pf = poblacion[cont]
              }
              if(i == input$T0 + 7){
                p5 = poblacion[cont]
              }
              cont = cont +1
            }
          }
        }
        t = input$Tf-input$T0
        k = log(p5/p0)/(7)
        res = 0
        if(input$Modelo==1){
          res = malthus(t, k, p0)
        }
        else{
          res = logistico(t, k, p0, input$Carga)
        }
        
        paste("La poblaciÃ³n para el Año ",input$Tf," de ", palabra," es: ", res)
      })
    })
  }
  
  ## FUNCIONES
  Graficar<-function(t0,tf,p0, pf, p5, modelo, carga, poblacion){
    #Numero de Años a graficar
    numYears = tf - t0
    x = seq(0, numYears)
  
    #Constante de crecimiento
    k = asNumeric(mpfr(log(p5/p0)/(7),128))
    #Capacidad de carga
    
    y = c()
    j=1
    #Calcular poblacion
    for (i in x){
      if(modelo==1){
        y[j] =  malthus(i,k, p0)
        j=j+1
      }
      else if(modelo==2){
        y[j] = logistico(i, k, p0, carga)
        j=j+1
      }
    }
    
    palabra = ""
    if(modelo==1){
      palabra = "Crecimiento de poblacion Modelo de Malthus"
    }
    else{
      palabra = "Crecimiento de poblacion Modelo de Logistico"
    }
    
    #Seleccionar datos exactos
    p = c()
    k=1
    bandera = TRUE
    for (i in poblacion){
      if(i==p0){
        bandera = FALSE
      }
      if(bandera == FALSE){
        p[k]=i
        k =k+1
      }
      if(i ==pf){
        break;
      }
    }
    
    #Calculo de error
    
    err = c()
    media = c()
    errTr = c()
    efici = c()
    
    for (l in seq(0,length(p),1)) {
      if(l == 0){
        err[0] = 0
        media[0] = 0
        errTr[0] = 0
        efici[0] = 0
      } else {
        err[l] = (abs(y[l]-p[l]))/abs(y[l])
        media[l] = abs(y[l]+p[l])/2
        errTr[l] = abs(p[l-1]-p[l])/abs(y[l-1]-y[l])
        efici[l] = (p[l]*err[l])/p[l]
      }
    }
  
    
    par(mfrow=c(1,3))
    plot(x,y,xlab="tiempo (NÂº Años)",ylab="poblacion",main=palabra,type="l", col="black")
    lines( x, p, col = "red")
    lines( x, media, col = "green")
    legend("topleft", legend = c("Media", "Exactos", "SimulaciÃ³n"), col= 3:1, pch=1)
    
    plot(x, err, col = "red", type = "l", xlab="tiempo (NÂº Años)", ylab="Error", main = "Error relativo")
    plot(x, errTr, col = "red", type = "l", xlab="tiempo (NÂº Años)", ylab="Error", main = "Error de truncamiento")
    
    cat("\nEl error relativo acumulado es de: ",sum(err, na.rm = T))
    cat("\nEl error de truncamiento acumulado es de: ", sum(errTr, na.rm = T))
    cat("\nLa eficiencia es de: ", sum(efici, na.rm = T))
    malthus<-function(t, k, p0){
      return (p0*exp(k*t))
    }
    
    logistico<-function(t, k, p0, l){
      A = (l-p0)/p0
      return (l/(1+A*exp(-k*t)))
    }
    
    # Exponentes de Lyapunov Malthus 
    exponentes_Malthus <- function(n, x0)
    {
      exponentes <- c()
      i <- 1
      while(i <= n)
      {
        num <- malthus(1,2,3)
        Landa = 1/n*log((num^i)*(x0 + 1) - (num^i)*x0)
        exponentes[i] = Landa
        i <- i + 1 
      }
      
      return (exponentes) 
    }
    
    # Exponentes de Lyapunov Logistico
    exponentes_Logistico <- function(n, x0)
    {
      exponentes<-c()
      i <- 1
      while(i <= n)
      {
        num <- logistico(1, 2, 3, 6)
        Landa = 1/n*log((num^i)*(x0 + 1) - (num^i)*x0)
        exponentes[i] = Landa
        i <- i + 1 
      }
      return(exponentes) 
    }
    # Entropia de Kolmogrov-Sinaí Malthus
    sinai_malthus <- function(vect_malthus)
    {
      sinai <- 0
      i <- 1
      while(  i <= length(vect_malthus))
      {
        sinai <- vect_malthus[i] + sinai  
        i <- i + 1
      }
      
      return (sinai)
    }
    
    # Entropia de Kolmogrov-Sinaí Logistica
    sinai_logistico <- function(vect_log)
    {
      sinai <- 0
      i <- 1
      while(  i <= length(vect_log))
      {
        sinai <- vect_log[i] + sinai   
        i <- i + 1
      }
      
      return (sinai)
    }
    exponentes_Malthus(4, 2009)
    exponentes_Logistico(4, 2009) 
    
    EM <- exponentes_Malthus(4, 2009)
    EL <- exponentes_Logistico(4, 2009) 
    sinai_malthus(EM)
    sinai_malthus(EL)
    
  }
  
  malthus<-function(t, k, p0){
    return (p0*exp(k*t))
  }
  
  logistico<-function(t, k, p0, l){
    A = (l-p0)/p0
    return (l/(1+A*exp(-k*t)))
  }
  
  # Run the application 
  shinyApp(ui, server)
  
}
