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
RED = color(255, 0, 0)

#Render podría ser un archivo aparte. Este archivo importaría las funciones de utilidades y los métodos que ya se crearon en el archivo SR1.py.
class Render(object):
    #Puede quedar vacío. El width y el height son los parámetros que se le pasan al constructor; estos pueden existisr hasta el momento en el que se crea el window.
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.current_color = BLACK
        print("Color: ", self.current_color)
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
            self.framebuffer[x][y] = self.current_color #El color del punto es el color actual.
    

#Ponerlo en otro archivo.
class Obj(object):
    def __init__(self, filename):

        #Abriendo el archivo.
        with open(filename) as f:
            self.lines = f.read().splitlines() #Lee el archivo y lo separa por líneas.
            #self.lines = [line.split() for line in self.lines if line and line[0] != ' '] #Separa las líneas por espacios.

        #POr el momento solo se van a trabajar con las caras y con los vértices.
        self.vertices = []
        self.faces = []

        #print(self.lines)

        for line in self.lines:
            
            if not line or line.startswith("#"): #Si hay una línea vacía o una línea que tenga #, se salta. 
                continue



            prefix, value = line.split(' ', 1) #Se hace split con salto de línea de 1.
            #print(prefix, value)
                
            #prefix, value = lines.split(' ', 2) #Separa la línea por espacios. El 1 es para que solo separe una vez.
            #print(lines.split(' ', 1))
            
            #print("Línea llena: ", lines)
            #print()
    
            #prefix, value = line.split(' ', 1) #Separa la línea por espacios. El 1 es para que solo separe una vez.

            #print(prefix)
            #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            #print(value)

            #Todo tiene que ser en el Render. Prefix tiene que tener el v o f y value lo demás.

            #Arreglar este código.
            if prefix == 'v': #Si el prefijo es v, entonces es un vértice.
                
                #print("Vértice")
                #print(value)
                self.vertices.append(
                    list(
                        map(float, value.strip().split(' '))
                        )
                    ) #Se agrega el valor de la línea a la lista de vértices.

            #A cada cara se le quita el espacio, luego se le quita la diagonal y por último se convierten a entero.
            if prefix == 'f': #Si el prefijo es v, entonces es un vértice.
                #print("Cara")
                #print(value)
                #Quitar las / y las // porque hay obj's que pueden tener las dos.
                #Hacer un if con eso.
                try:
                    self.faces.append([
                        list(map(int, face.strip().split('/'))) #Quitando las diagonales.
                            for face in value.strip().split(' ')
                        ]
                    ) #Se agrega el valor de la línea a la lista de vértices.
                except:
                    self.faces.append([
                        list(map(int, face.strip().split('//'))) #Quitando las diagonales.
                            for face in value.strip().split(' ')
                        ]
                    )

            #print(self.faces)

r = Render(1024, 1024) #Crea un objeto render con un tamaño de 1024x1024.


#r.current_color = color(200, 100, 0) #Cambia el color actual a uno diferente.

r.current_color = RED #Cambia el color actual a rojo.

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

    #Quitando decimales.
    x0 = round(x0)
    x1 = round(x1)
    y0 = round(y0)
    y1 = round(y1)
    
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
    dy = abs(y1 - y0)
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

#Hacer mejor esta parte.

"""
#Matriz del cuadrado.
square = [
    (100, 100),
    (200, 100),
    (200, 200),
    (100, 200)
]

center = (150, 150) #Centro del cuadrado.

#Moviendo el cuadrado a la derecha.
square_large = [
    (
        ((x - center[0]) * 1.5) + center[0], 
        ((y - center[1]) * 3.5) + center[1]
    ) 
    for x, y in square
]

tsquare = square_large #Cuadrado temporal. 

last_point = tsquare[-1] #Último punto.

#Dibujando el cuadrado.
for point in tsquare:
    line(*last_point, *point) #Dibuja una línea.
    #print(last_point, point)
    last_point = point #Último punto.
"""
cube = Obj('FuelTruck.obj') #Crea un objeto "o" con el archivo "cube.obj".

#Función que transforma el vértice.
def transform_vertex(vertex, scale, translate):
    #print("Vertex: ", vertex)
    return [
        (
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1] #Y.
        )
    ]

scale_factor = (5, 5) #Factor de escala. Esto es algo que se tiene que recibir en la función.
translate_factor = (512, 512) #Traslación. Esto es algo que se tiene que recibir en la función.

#Recorriendo las caras e imprimiéndolas.
for face in cube.faces: 
    #print("Face: ", face)
    if len(face) == 4: 
        
        f1 = face[0][0] - 1 #Restando uno para estar en el índice correcto.
        f2 = face[1][0] - 1 #Restando uno para estar en el índice correcto.
        f3 = face[2][0] - 1 #Restando uno para estar en el índice correcto.
        f4 = face[3][0] - 1 #Restando uno para estar en el índice correcto.

        v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor) #Obteniendo el vértice 1.
        v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor) #Obteniendo el vértice 2.
        v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor) #Obteniendo el vértice 3.
        v4 = transform_vertex(cube.vertices[f4], scale_factor, translate_factor) #Obteniendo el vértice 4.


        line(
            v1[0][0], #X del vértice 1.
            v1[0][1], #Y del vértice 1.
            v2[0][0], #X del vértice 2.
            v2[0][1]  #Y del vértice 2.
        ) #El vértice 1 es el índice 0 del array.

        line(
            v2[0][0], #X del vértice 2.
            v2[0][1], #Y del vértice 2.
            v3[0][0], #X del vértice 3.
            v3[0][1]  #Y del vértice 3.
        )

        line(
            v3[0][0], #X del vértice 3.
            v3[0][1], #Y del vértice 3.
            v4[0][0], #X del vértice 4.
            v4[0][1]  #Y del vértice 4.
        )

        line(
            v4[0][0], #X del vértice 4.
            v4[0][1], #Y del vértice 4.
            v1[0][0], #X del vértice 1.
            v1[0][1]  #Y del vértice 1.
        )

    if len(face) == 3: 

        f1 = face[0][0] - 1 #Restando uno para estar en el índice correcto.
        f2 = face[1][0] - 1 #Restando uno para estar en el índice correcto.
        f3 = face[2][0] - 1 #Restando uno para estar en el índice correcto.
        #f4 = face[3][0] - 1 #Restando uno para estar en el índice correcto.

        v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor) #Obteniendo el vértice 1.
        v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor) #Obteniendo el vértice 2.
        v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor) #Obteniendo el vértice 3.
        #v4 = transform_vertex(cube.vertices[f4], scale_factor, translate_factor) #Obteniendo el vértice 4.


        line(
            v1[0][0], #X del vértice 1.
            v1[0][1], #Y del vértice 1.
            v2[0][0], #X del vértice 2.
            v2[0][1]  #Y del vértice 2.
        ) #El vértice 1 es el índice 0 del array.

        line(
            v2[0][0], #X del vértice 2.
            v2[0][1], #Y del vértice 2.
            v3[0][0], #X del vértice 3.
            v3[0][1]  #Y del vértice 3.
        )

        line(
            v3[0][0], #X del vértice 3.
            v3[0][1], #Y del vértice 3.
            v1[0][0], #X del vértice 4.
            v1[0][1]  #Y del vértice 4.
        )
    
    #break

#print(o.lines) #Imprime las líneas del archivo "cube.obj".

#r.point(10, 10) #Dibuja un punto en la pantalla.
#line(13, 20, 50, 50) #Dibuja una línea en la pantalla.
#line(20, 13, 40, 80) #Dibuja una línea en la pantalla.
#line(80, 40, 13, 20) #Dibuja una línea en la pantalla.
r.write("a.bmp") #Escribe el archivo. El nombre del archivo es a.bmp, porque se le pasa una cadena de caracteres.