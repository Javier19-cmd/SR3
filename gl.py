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

from Render import * #Importando la clase Render.
from utilidades import *


c1 = Render() #Inicializando la clase Render.

#Pregunar si está bien implementada esta función.
def glInit(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.

    #Importar la clase de Render.
    #r = Render.Render(ancho, alto, glClear(), glColor(0.003, 1, 0.019)) #Creando el color de la línea.) #Creando el framebuffer con el color que se le pasa.
    pass

def glCreateWindow(width, height): #Preguntar de esta función.
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)

    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Creando las dimensiones de la pantalla.

            c1.width = width #Ancho de la pantalla.
            c1.height = height #Alto de la pantalla.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.

    colorV = color(0.4, 0.8, 0.08) #Creando el color del viewport.

    #Verificando que las dimensiones del viewport sean múltiplos de 4.
    if width % 4 == 1 and height % 4 == 1:
        
        c1.colorViewPort = colorV #Se manda a hacer el color del viewport.

        c1.View(x, y, width, height) #Se manda a hacer el viewport.
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
    

    #print("Colores en glClear ", color(rP, gP, bP)) #Imprimiendo el color que se le pasa.
    
    # if rP < 0 or gP < 0 or bP < 0: #Si los colores son menores a 0, entonces se imprime un error.
    #     print("Error")
    # elif rP > 1 or gP > 1 or bP > 1:
    #     print("Error")
    # else: #Si todo está bien, entonces se llena el mapa de bits con el color que se le pasa.
    #     #print(color(rP, gP, bP))
    
    c1.Framebuffer() #Llenando el framebuffer con el color que se le pasó en glClearColor.

    #Debugging.
    #print(anchoV)
    #print(altoV) 
    #print(Rend.Render.framebuffer)

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
        
    #Verificando que los códigos de los colores no sean negativos.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1: #Verificando que los códigos de los colores no sean mayores a 255.
        print("Error")
    else: #Si todo está bien, entonces se crea el framebuffer con el color que se le pasa.
        
        #print("Color de fondo antes: ", c1.colorFondo) #Antes de cambiar el color, se imprime el color de fondo.
        
        colorPantalla = color(r, g, b) #Creando el color de la pantalla.
        
        c1.colorFondo = colorPantalla #Se manda a hacer el color de la pantalla.

        #print("Color de fondo: ", c1.colorFondo) #Imprimiendo el color de la pantalla.

        #color(rP, gP, bP) #Color inicial de la pantalla.
       
        #Rend2.recibirColor(color(rP, gP, bP))

        #print("Color en glClearColor: ", color(rP, gP, bP)) #Debuggeo.

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    #Ubicar un punto en el viewport.
    
    #Obteniendo el centro del viewport.
    x0 = int(c1.xV + (c1.widthV/2))
    y0 = int(c1.yV + (c1.heightV/2))

    #Moviendo el punto a la posición deseada.
    movx = x0 + int(x * (c1.widthV/2))
    movy = y0 + int(y * (c1.heightV/2))

    #Debuggeo.
    print("Posiciones del punto trasladado ", movx, movy)

    #print("Hola ", movx, movy) #Debugging.

    c1.Vertex(movx, movy) #Creando el punto.


"""
def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    #Ubicar un punto en el viewport.

    

    #Debuggeo.
    print("Posiciones del punto trasladado ", x, y)

    #print("Hola ", movx, movy) #Debugging.

    if(0 < x < ancho) and (0 < y < alto):

        c1.Vertex(x, y) #Creando el punto.
"""

#Función que crea una línea entre dos puntos. Esta tiene que estar en el rango de 0 a 1.
def glLine(x0, y0, x1, y1):
    #global ancho, alto, equis, ye #Variables globales que se usarán para definir el área de la imagen sobre la que se va a poder dibujar el punto.

    #Verifiando las propiedades del viewport.
    #print(ancho, alto, equis, ye)
    
    #Obteniendo el centro del viewport.
    x = int(c1.xV + (c1.widthV/2))
    y = int(c1.yV + (c1.heightV/2))

    #Obteniendo las coordenadas de x0 y y0 con respecto al viewport.
    movx1 = x + int(x0 * (c1.widthV/2))
    movy1 = y + int(y0 * (c1.heightV/2))

    #Obteniendo las coordenadas de x1 y y1 con respecto al viewport.
    movx2 = x + int(x1 * (c1.widthV/2))
    movy2 = y + int(y1 * (c1.heightV/2))

    #Moviendo el punto a la posición deseada.
    # dy = abs(y1 - y0)
    # dx = abs(x1 - x0)

    print("Posiciones del viewport ", c1.xV, c1.yV)

    #Prueba.
    dx1 = abs(movx2 - movx1)
    dy1 = abs(movy2 - movy1)

    #Debuggeo.
    #print("Cambio en y y cambio en x ", dy, dx)
    #print("Cambio en x y cambio en y ", dx1, dy1)


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
    for x in range(movx1, movx2 + 1):
        
        offset += dy * 2 #Cambiando el offset.
        if offset >= threshold: #Si el offset es mayor o igual al umbral, entonces se cambia la coordenada y.
            y += 1 if movy1 < movy2 else -1
            threshold += 2 * dx

            #print("Punto inicial: ", movx1, movy1)
            #print("Punto final: ", movx2, movy2)

        if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
            #print(y, x)
            #Rend2.Line(y, x)
            #print("Puntos dados en decimales ", x0, y0, x1, y1)
            c1.Vertex(y, x)
            #glVertex(y, x)
        else: #Si la línea es horizontal, entonces se cambia el orden de los puntos.
            #print(x, y)
            #Rend2.Line(x, y)
            #print("Puntos dados en decimales ", x0, y0, x1, y1)
            c1.Vertex(x, y)
            #glVertex(x, y)

"""
#Función que crea una línea entre dos puntos. Esta tiene que estar en el rango de 0 a 1.
def glLine(x0, y0, x1, y1):


    #Redondeo para que no haya problemas con los decimales.
    x0 = round(x0)
    y0 = round(y0)
    x1 = round(x1)
    y1 = round(y1)


    #Verifiando las propiedades del viewport.
    #print(ancho, alto, equis, ye)
    
    #Moviendo el punto a la posición deseada.
    # dy = abs(y1 - y0)
    # dx = abs(x1 - x0)

    #print("Posiciones: ", x0, y0, x1, y1)

    #Prueba.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    #Debuggeo.
    #print("Cambio en y y cambio en x ", dy, dx)
    #print("Cambio en x y cambio en y ", dx1, dy1)


    steep = dy > dx #Verificando si la línea es vertical o horizontal.

    if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    
    if x0 > x1: #Si el punto 1 está a la derecha del punto 2, entonces se cambia el orden de los puntos.
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Calculando los nuevos cambios.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    offset = 0 #Offset de la línea.
    threshold = dx #Umbral de la línea.	
    y = y0 #Coordenada y de la línea.

    #Verificando las variables.
    #print("Offset, threshold, y ",offset, threshold, y)

    #Dibujando la línea.
    for x in range(x0, x1 + 1):
        
        offset += dy * 2 #Cambiando el offset.
        if offset >= threshold: #Si el offset es mayor o igual al umbral, entonces se cambia la coordenada y.
            y += 1 if y0 < y1 else -1
            threshold += 2 * dx

            #print("Punto inicial: ", movx1, movy1)
            #print("Punto final: ", movx2, movy2)

        if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
            #print(y, x)
            #Rend2.Line(y, x)
            #print("Puntos dados en decimales ", x0, y0, x1, y1)
            c1.Vertex(y, x)
            #glVertex(y, x)
        else: #Si la línea es horizontal, entonces se cambia el orden de los puntos.
            #print(x, y)
            #Rend2.Line(x, y)
            #print("Puntos dados en decimales ", x0, y0, x1, y1)
            c1.Vertex(x, y)
            #glVertex(x, y)
"""

def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    
    global Color #Se usa para poder acceder a las variables globales.
    
    #Convertir el valor de 0 a 1 de 0 a 255 y luego llamar al color.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1:
        print("Error")
    else:
        
        #print("Color antes de ser cambiado: ", c1.colorP)
        Color = color(r, g, b) #Se manda a hacer el color con las utilidades y se setea el color.
        #print("Color en gl: ", Color)
        c1.colorP = Color #Se setea el color del punto.
        #print("Color cambiando en el Render: ", c1.colorP)

        #print("El color del punto es: ", Color)
def glFinish(): #Función que escribe el archivo de imagen resultante.
    #print(altoV, anchoV)
    #Rend2.write()
    #pass
    #print(rP, gP, bP)
    #Llamar al método write en la clase Render.
   # Rend.write()

   #Rend2.punto(25, 25) #Probando el método punto.
   c1.write() #Escribiendo el archivo.

#print(glColor(1,1,1))

#print(glClearColor(1,1,1))

#print(glColor(0.9, 0.8, 0.87))
