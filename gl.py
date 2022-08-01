"""
#Nombre: Javier Valle
#Carnet: 20159

Referencias: 

1. Instanciar un archivo de Python: https://www.youtube.com/watch?v=rYcluou5gEo&ab_channel=LuisCabreraBenito
2. Saber si un número es múltiplo de otro: https://www.youtube.com/watch?v=jOCh6ZpkE1k&ab_channel=JohnOrtizOrdoñez
3. Hacer un return de múltiples variables: https://www.youtube.com/watch?v=QOQTYuynU3w&ab_channel=ProgramaResuelto
4. Formato de archivo BMP: https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20BMP%20file%20format%2C%20also,and%20OS%2F2%20operating%20systems. 
5. Acceder a una variable de otra clase: https://programmerclick.com/article/14131486210/
6. Algoritmo de Lineas Bresenham: https://es.wikipedia.org/wiki/Algoritmo_de_Bresenham#:~:text=El%20Algoritmo%20de%20Bresenham%20es,solo%20realiza%20cálculos%20con%20enteros.
7. Algoritmo de Bresenham: https://www.youtube.com/watch?v=yaovJmM-0OM&ab_channel=CodesVille
8. Simular un do-while: https://www.freecodecamp.org/espanol/news/python-bucle-do-while-ejemplos-de-bucles/#:~:text=Para%20crear%20un%20bucle%20do%20while%20en%20Python%2C%20necesitas%20modificar,verdadero%20se%20ejecutará%20otra%20vez.
"""

import Render as Rend2 #Importando la clase Render.
from utilidades import *

#Variables globales.
anchoV = 0 #Ancho de la ventana.
altoV = 0 #Alto de la ventana.


#Color de la pantalla.
rP = 0
gP = 0
bP = 0
fondo = 0

#Ubicaciones del viewport.
equis = 0
ye = 0

#Variable global para la función glColor.
Color = 0

#Variables para la línea.
equis0 = 0
ye0 = 0
equis1 = 0
ye1 = 0

#Pregunar si está bien implementada esta función.
def glInit(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.

    #Importar la clase de Render.
    #r = Render.Render(ancho, alto, glClear(), glColor(0.003, 1, 0.019)) #Creando el color de la línea.) #Creando el framebuffer con el color que se le pasa.
    pass

def glCreateWindow(width, height): #Preguntar de esta función.
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)
    global anchoV, altoV #Variables globales, que servirán para definir el tamaño de la imagen resultante.

    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Llenando variables globales. Estas son para el ancho de la ventana y el alto de la ventana.
            anchoV = width 
            altoV = height

            Rend2.DimensionesPantalla(anchoV, altoV) #Creando la ventana.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.
    global ancho, alto, equis, ye #Variables globales que se usarán para definir el área de la imagen sobre la que se va a poder dibujar.

    #Todas las variables que se reciben se guardan en variables globales.
    ancho = width
    alto = height
    equis = x
    ye = y

    colorV = color(0.4, 0.8, 0.08) #Creando el color del viewport.

    Rend2.colorViewPort(colorV) #Recibiendo el color del viewport.

    #Verificando que las dimensiones del viewport sean múltiplos de 4.
    if ancho % 4 == 1 and alto % 4 == 1:
        Rend2.View(equis, ye, ancho, alto)
    else: 
        print("Error")

#Rend2.View(equis, ye, ancho, alto) #Creando el viewport.
#Variables para crear la ventana.
#dimensiones = [glViewPort(1, 2, 100, 200)] #Se inicializan las dimensiones de la ventana en una lista.
#Imprimiendo las dimensiones de la imagen.
#print(dimensiones)

#ancho = dimensiones[0][2] #Sacando el ancho de la imagen.
#alto = dimensiones[0][3] #Sacando el alto de la imagen.

#Preguntar si esta función lo que hace es llenar por primera vez el color de la pantalla.
def glClear(): #Se usará para que llene el mapa de bits con un solo color.   
    global fondo #Variable global para el color del fondo de pantalla.

    #print("Colores en glClear ", color(rP, gP, bP)) #Imprimiendo el color que se le pasa.
    
    # if rP < 0 or gP < 0 or bP < 0: #Si los colores son menores a 0, entonces se imprime un error.
    #     print("Error")
    # elif rP > 1 or gP > 1 or bP > 1:
    #     print("Error")
    # else: #Si todo está bien, entonces se llena el mapa de bits con el color que se le pasa.
    #     #print(color(rP, gP, bP))
    
    fondo = color(rP, gP, bP) #Creando el color de la línea.

    Rend2.recibirColorFondo(fondo) #Recibiendo el color del fondo.
    Rend2.Framebuffer() #Llenando el framebuffer de la pantalla.

    #Debugging.
    #print(anchoV)
    #print(altoV) 
    #print(Rend.Render.framebuffer)

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
    
    global rP, gP, bP #Se usa para poder acceder a las variables globales.

    #global Render #Se usa para poder acceder a la variable global render.
    
    #Verificando que los códigos de los colores no sean negativos.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1: #Verificando que los códigos de los colores no sean mayores a 255.
        print("Error")
    else: #Si todo está bien, entonces se crea el framebuffer con el color que se le pasa.
        
        #Llenando variables globales.
        rP = r
        gP = g
        bP = b

        #color(rP, gP, bP) #Color inicial de la pantalla.
       
        #Rend2.recibirColor(color(rP, gP, bP))

        #print("Color en glClearColor: ", color(rP, gP, bP)) #Debuggeo.

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    #Ubicar un punto en el viewport.
    global ancho, alto, equis, ye #Variables globales que se usarán para definir el área de la imagen sobre la que se va a poder dibujar el punto.

    #Verifiando las propiedades del viewport.
    print(ancho, alto, equis, ye)
    
    #Obteniendo el centro del viewport.
    x0 = int(equis + (ancho/2))
    y0 = int(ye + (alto/2))

    #Moviendo el punto a la posición deseada.
    movx = x0 + int(x * (ancho/2))
    movy = y0 + int(y * (alto/2))

    #Debuggeo.
    print("Posiciones del punto trasladado ", movx, movy)

    #print("Hola ", movx, movy) #Debugging.

    Rend2.Vertex(movx, movy) #Creando el punto.

#Función que crea una línea entre dos puntos. Esta tiene que estar en el rango de 0 a 1.
def glLine(x0, y0, x1, y1):
    global ancho, alto, equis, ye #Variables globales que se usarán para definir el área de la imagen sobre la que se va a poder dibujar el punto.

    #Verifiando las propiedades del viewport.
    print(ancho, alto, equis, ye)
    
    #Obteniendo el centro del viewport.
    x = int(equis + (ancho/2))
    y = int(ye + (alto/2))

    #Obteniendo las coordenadas de x0 y y0 con respecto al viewport.
    movx1 = x + int(x0 * (ancho/2))
    movy1 = y + int(y0 * (alto/2))

    #Obteniendo las coordenadas de x1 y y1 con respecto al viewport.
    movx2 = x + int(x1 * (ancho/2))
    movy2 = y + int(y1 * (alto/2))

    #Moviendo el punto a la posición deseada.
    # dy = abs(y1 - y0)
    # dx = abs(x1 - x0)

    print("Posiciones del viewport ", equis, ye)

    #Prueba.
    dx1 = abs(movx2 - movx1)
    dy1 = abs(movy2 - movy1)

    #Debuggeo.
    #print("Cambio en y y cambio en x ", dy, dx)
    print("Cambio en x y cambio en y ", dx1, dy1)


    steep = dy1 > dx1 #Verificando si la línea es vertical o horizontal.

    if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
        movx1, movy1 = movy1, movx1
        movx2, movy2 = movy2, movx2
    
    if movx1 > movx2: #Si el punto 1 está a la derecha del punto 2, entonces se cambia el orden de los puntos.
        movx1, movx2 = movx2, movx1
        movy1, movy2 = movy2, movy1

    #Calculando los nuevos cambios.
    dx = abs(movx2 - movx1)
    dy = abs(movy2 - movy1)

    offset = 0 #Offset de la línea.
    threshold = dx #Umbral de la línea.	
    y = movy1 #Coordenada y de la línea.

    #Verificando las variables.
    #print("Offset, threshold, y ",offset, threshold, y)

    #Dibujando la línea.
    for x in range(movx1, movx2):
        
        offset += dy * 2 #Cambiando el offset.
        if offset >= threshold: #Si el offset es mayor o igual al umbral, entonces se cambia la coordenada y.
            y += 1 if movy1 < movy2 else -1
            threshold += 2 * dx

            print("Punto inicial: ", movx1, movy1)
            print("Punto final: ", movx2, movy2)

        if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
            print(y, x)
            #Rend2.Line(y, x)
            print("Puntos dados en decimales ", x0, y0, x1, y1)
            Rend2.Vertex(y, x)
            #glVertex(y, x)
        else: #Si la línea es horizontal, entonces se cambia el orden de los puntos.
            #print(x, y)
            #Rend2.Line(x, y)
            print("Puntos dados en decimales ", x0, y0, x1, y1)
            Rend2.Vertex(x, y)
            #glVertex(x, y)


def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    
    global Color #Se usa para poder acceder a las variables globales.
    
    #Convertir el valor de 0 a 1 de 0 a 255 y luego llamar al color.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1:
        print("Error")
    else:
        Color = color(r, g, b) #Se manda a hacer el color con las utilidades y se setea el color.
        print(Color)
        Rend2.colorPunto(Color)
        #print("El color del punto es: ", Color)
def glFinish(): #Función que escribe el archivo de imagen resultante.
    #print(altoV, anchoV)
    #Rend2.write()
    #pass
    #print(rP, gP, bP)
    #Llamar al método write en la clase Render.
   # Rend.write()

   #Rend2.punto(25, 25) #Probando el método punto.
   Rend2.write() #Escribiendo el archivo.

#print(glColor(1,1,1))

#print(glClearColor(1,1,1))

#print(glColor(0.9, 0.8, 0.87))
