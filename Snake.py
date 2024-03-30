import turtle
import time
import random

posponer = 0.1

#Marcador
Puntuación = 0
Puntuación_mas_alta = 0

#Configuracion de la ventana 
snake = turtle.Screen()
snake.title("Juego de la Viborita (^///^.)")  
snake.bgcolor("black")                     
snake.setup(width=600, height=600)          
snake.tracer(0)        

#Cabeza de la serpiente 
C_Serpiente = turtle.Turtle()
C_Serpiente.speed(0)  #Velocidad a la que se inicia el movimiento de ka serpiente
C_Serpiente.shape("square")      
C_Serpiente.color("green") #Color de el cuerpo de la vibora 
C_Serpiente.penup()               #Para que no se dibuje en el suelo
C_Serpiente.goto(0,0) #Posicion de inicializacion de la Serpiente 
C_Serpiente.direccion = "stop"    

#Comida de la serpiente 
ComidaSerp = turtle.Turtle()
ComidaSerp.speed(0)  #Velocidad a la comida
ComidaSerp.shape("circle")      
ComidaSerp.color("Red") #Color de la comida de la Serpiente
ComidaSerp.penup()               #Para que no se dibuje en el suelo
ComidaSerp.goto(0,100) #Posicion de inicializacion de la comida de la serpiente 
   
#Curpo de la serpiente / segmentos de la misma 
CuerpoSeg = []

#Texto de ña pantalla 
textP = turtle.Turtle()
textP.speed(0)
textP.color("white")
textP.penup()
textP.hideturtle()
textP.goto(0,260)
textP.write(f'Puntuación: 0           Puntuación más alta: 0', align='center', font=('Bold', 15))


#Funciones de la Serpiente 

def Ariba():
    C_Serpiente.direccion = "up"
    
def Abajo():
    C_Serpiente.direccion = "down"
    
def Izquierda():
    C_Serpiente.direccion = "left"
    
def Derecha():
    C_Serpiente.direccion = "right"

#Movimiento de la serpiente 
def movSer():
    if C_Serpiente.direccion == "up":
        y = C_Serpiente.ycor()
        C_Serpiente.sety(y + 10)
        
    if C_Serpiente.direccion == "down":
        y = C_Serpiente.ycor()
        C_Serpiente.sety(y - 10)
        
    if C_Serpiente.direccion == "left":
        x = C_Serpiente.xcor()
        C_Serpiente.setx(x - 10)
        
    if C_Serpiente.direccion == "right":
        x = C_Serpiente.xcor()
        C_Serpiente.setx(x + 10)

#Conecion con teclado
snake.listen()
snake.onkeypress(Ariba, "Up")
snake.onkeypress(Abajo, "Down")
snake.onkeypress(Izquierda, "Left")
snake.onkeypress(Derecha, "Right")
#Bucle de el juego 
while True:
    snake.update()
    #Colision con su bordes 
    if C_Serpiente.xcor() > 280 or C_Serpiente.xcor() < -280 or C_Serpiente.ycor() > 280 or C_Serpiente.ycor() < -280:
        time.sleep(1)
        C_Serpiente.goto(0,0)
        C_Serpiente.direccion = "stop"
        
        #Segmentos separados 
        for Cuerpo in CuerpoSeg:
            Cuerpo.goto(1000, 1000)
            
            #Limpiar la Lista 
        CuerpoSeg.clear()
        #Resetea la puntuacion 
        Puntuación = 0
        textP.clear()
        textP.write(f'Puntuación: {Puntuación}           Puntuación más alta: {Puntuación_mas_alta}', align='center', font=('Bold', 15))

               
        
        #Reseteo de del puntuador cuando se choa con los bordes 
        
    
    if C_Serpiente.distance(ComidaSerp) <15:
       x = random.randint(-280, 280)
       y = random.randint(-280, 280)
       ComidaSerp.goto(x,y)
       
       NuevoSeg = turtle.Turtle()
       NuevoSeg.speed(0)  
       NuevoSeg.shape("square")      
       NuevoSeg.color("yellow", "Red") #Color de el cuerpo de la vibora 
       NuevoSeg.penup()               #Para que no se dibuje en el suelo
       CuerpoSeg.append(NuevoSeg)      #Se agrega a la lista del cuerpo de la vibora
       
       #Aumenta el marcador  al comerse una comida
       Puntuación += 10
    
       if Puntuación > Puntuación_mas_alta:
               Puntuación_mas_alta = Puntuación
               
               textP.clear()
               textP.write(f'Puntuación: {Puntuación}           Puntuación más alta: {Puntuación_mas_alta}', align='center', font=('Bold', 15))

               
     #Mover cuerpo de la Vibora 
    SegTotal = len(CuerpoSeg)          #Numero total de segmentos del cuerpo de la vibora
    for index in range(SegTotal-1, 0, -1):    #Recorre todos los segmentos menos el ultimo uno
         x = CuerpoSeg [index -1].xcor()
         y = CuerpoSeg [index -1].ycor()
         CuerpoSeg [index].goto(x,y)
         
    if SegTotal >0:
        x = C_Serpiente.xcor()
        y = C_Serpiente.ycor()
        CuerpoSeg[0].goto(x,y)
        
    movSer()
         #Colisiones con el cuerpo  de la vibora
    for Cuerpo in CuerpoSeg:
      if C_Serpiente.distance(Cuerpo) <1 :
        time.sleep(1)
        C_Serpiente.goto(0,0)
        C_Serpiente.direccion = "stop"
        
        #Esconder Segmentos
        for Cuerpo in CuerpoSeg:
            Cuerpo.goto(1000, 1000)
            
            #Limpiar la Lista 
        CuerpoSeg.clear()
        #Resetea la puntuacion 
        Puntuación = 0
        textP.clear()
        textP.write(f'Puntuación: {Puntuación}           Puntuación más alta: {Puntuación_mas_alta}', align='center', font=('Bold', 15))

               
        
        
          
    time.sleep(posponer)
    
    
#MR360

