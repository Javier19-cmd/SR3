import struct

#Set de utilidades. Estas funciones se pueden hacer en otro archivo para mayor comodidad.

#Se usa el = para convertir de manera correcta.

#Recibe un string y lo convierte en una lista de bytes.
def char(c):
    #Ocupa 1 byte.
    #=c es para que sea un caracter. El encode es para convertir el caracter a bits. El =c es para convertir esos bits a bytes.
    return struct.pack("=c", c.encode('ascii'))

#Recibe un número como parámetro.
def word(w):
    #Ocupa 2 bytes.
    #El formato para un word es 'h'. Este gasta 2 bytes, que es lo que se quiere.
    return struct.pack("=h", w)

#Recibe un número como parámetro.
def dword(d): #Double word.
    #Ocupa 4 bytes. El l es para un num de 4 bytes.
    return struct.pack("=l", d)

def color(r, g, b): #Función que crea el color.
    #3 bytes. Retorna el color en bytes.
    return bytes([b, g, r])

#Colorea un punto de la imagen.
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

#Render podría ser un archivo aparte. Este archivo importaría las funciones de utilidades y los métodos que ya se crearon en el archivo SR1.py.
class Render(object):
    #Puede quedar vacío. El width y el height son los parámetros que se le pasan al constructor; estos pueden existisr hasta el momento en el que se crea el window.
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.current_color = WHITE
        self.clear() #Limpiar la pantalla.
    
    #Método que se usará para llenar de bits la pantalla.
    def clear(self):
        #Generador del color.
        self.framebuffer = [
            #Los colores tienen que ir de 0 a 255.
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def write(self, filename):
        #Esta no necesita recibir ningún nombre de archivo.
        #Abrir en bw: binary write.
        f = open(filename, "bw")
        
        #Pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Tamaño del archivo en bytes. 
        # El 3 es para los 3 bytes que seguirán. El 14 es el tamaño del infoheader y el 40 es el tamaño del otro header.
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0)) #Algo que no se usará. Este es de 2 bytes, por eso se utiliza el word.
        f.write(word(0)) #Algo que no se usará. Este es de 2 bytes, por eso se utiliza el word.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.
        
        #Info header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        
        #Pixel data.
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[y][x])
        f.close()

    #Función que dibuja un punto en la pantalla. Esta es una función de bajo nivel. 
    def point(self, x, y): 

        if (0 < x < self.width) and (0 < y < self.height):

            #Esta función dibuja un punto en la pantalla.
            self.framebuffer[y][x] = self.current_color #El color del punto es el color actual.
    

r = Render(100, 100) #Crea un objeto render con un tamaño de 1024x1024.


#r.current_color = color(200, 100, 0) #Cambia el color actual a uno diferente.

r.current_color = WHITE #Cambia el color actual a blanco.

"""
#Esto hace la línea en diagonal.
for x in range(100, 200):
    for x in range(100, 200):
        r.current_color = color(
            255, 
            255,
            255) #Cambia el color actual a uno diferente.
        r.point(x, x) #Dibuja un cuadrado en la pantalla.
"""

#r.current_color = color(100, 100, 255) #Cambia el color actual a uno diferente.
"""
for x in range(300, 400):
    for y in range(300, 400):
        r.point(x, y) #Dibuja un cuadrado en la pantalla.
"""


def line(x0, y0, x1, y1): #Función que dibuja una línea.
    
    dy = abs(y1 - y0) #Calcula la distancia entre los puntos.
    dx = abs(x1 - x0) #Calcula la distancia entre los puntos.
   # m = (dy / dx) * dx

    steep = dy > dx #Si la línea es más ancha que alta.


    if steep: #Si la línea es más ancha que alta.
        x0, y0 = y0, x0 #Intercambia los valores de "x0" y "y0". Esto es para que la línea se dibuje correctamente.
        x1, y1 = y1, x1 #Intercambia los valores de "x0" y "y0". Esto es para que la línea se dibuje correctamente.

    if x0 > x1: #Si x0 es mayor que x1.
        x0, x1 = x1, x0 #Intercambia los valores de "x0" y "x1". Esto es para que la línea se dibuje correctamente.
        y0, y1 = y1, y0 #Intercambia los valores de "y0" y "y1". Esto es para que la línea se dibuje correctamente.
    
    #Si la línea es más ancha que alta.
    dy = y1 - y0
    dx = x1 - x0
    #m = (dy / dx) * dx * 2

    offset = 0 #Offset de la línea.
    threshold = dx #Umbral de la línea.
    y = y0 #Y de la línea.
    
    #Recta: y = y0 + m * (x - x0)

    for x in range(x0, x1):
        
        offset += dy * 2 #Offset de la línea.
        
        if offset >= threshold: #Si el offset es mayor o igual al umbral.
            y += 1 if y0 < y1 else -1 #Decrementa la y.
            threshold +=  dx * 2 #Aumenta el umbral.

        if steep: #Si la línea es más ancha que alta.
            r.point(y, x)
        else: #Si la línea es más alta que ancha.
            r.point(x, y)


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f: 
            #Dado un archivo, lee todo el archivo y lo guarda en una lista.
            self.lines = f.read().splitlines()

            #Por el momento, sólo se trabajará con los vértices.
            self.vertices = []
            self.faces = []

            for line in self.lines:
                prefix, value = line.split(' ', 1) #Separa en el primer espacio.

                
                if prefix == 'v': #Si es un vértice.
                    self.vertices.append(
                        list(
                            map(float, value.split(' ')
                            )
                        )
                    )
                
                if prefix == 'f': #Si es una cara.
                    self.faces.append(
                        list(
                            map(
                                float, value.split(' ')
                            )
                        )
                    )

    #i = 0
    #while i <= 1:
     #   x = x0 + i * (x1 - x0)
     #   y = y0 + i * (y1 - y0)
     #   r.point(round(x), round(y))
     #   #i += 0.0001 #Número sacado de la manga.
     #   i += 0.1 #Número sacado de la manga.

#Matriz para dibujar un cuadrando.
square = [
    [100, 100],
    [200, 100],
    [200, 200],
    [100, 100]
]

center = (150, 150)

square_large = [
    ((x - center[0]) * 0.5,
     (y - center[1]) * 0.5) 
    for x, y, in square
]


#Trasladar el cuadrado a la derecha.
square_right = [
    [199, 100],
    [199, 100],
    [199, 200],
    [199, 100]
]

tsquare = square_large


#Último punto.
last_point = tsquare[-1]


#Dibujar el cuadrado.
for point in square: 
    line(*last_point, *point)
    last_point = point

o = Obj("obj.obj")

#r.point(10, 10) #Dibuja un punto en la pantalla.
#line(13, 20, 50, 50) #Dibuja una línea en la pantalla.
#line(20, 13, 40, 80) #Dibuja una línea en la pantalla.
#line(80, 40, 13, 20) #Dibuja una línea en la pantalla.
r.write("a.bmp") #Escribe el archivo. El nombre del archivo es a.bmp, porque se le pasa una cadena de caracteres.