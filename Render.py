from utilidades import * #Archivo de utilidades.

class Render(object):

    def __init__(self, width, height): #Constructor de la clase.

        # Recibiendo las dimensiones de la pantalla.
        self.width = width
        self.height = height
        #Creando color genérico para el framebuffer.
        WHITE = color(1, 1, 1) #Color blanco hecho con las utilidades.
        self.colorFondo = WHITE #Asignando el color blanco al framebuffer.
        self.colorP = WHITE #Asignando el color blanco al punto.



    #Método que escribe el framebuffer.
    def Framebuffer(self):

        #print(colorP)

        #print(colorP)


        #Llenando de bits el framebuffer.
        self.framebuffer = [
            [self.colorFondo for x in range(self.width)]
            for y in range(self.width)
        ]


    #Método que dibuja un punto.
    def punto(self,x, y):
        #En este método se dibuja un punto en la pantalla.
        global equis, ye #Instanciando las variables globales de las posiciones del punto.

        #Llenando las variables globales.
        equis = x
        ye = y

        #Esta función dibuja un punto en la pantalla.
        #print(framebufobsfer[x][y])

        self.framebuffer[y][x] = self.colorP #El color del punto es el color actual.

    def colorViewPort(color):
        #En este método se setea el color del viewport.
        global colorV #Instanciando la variable global del color del viewport.

        #Llenando la variable global.
        colorV = color
        print("Color del viewport", colorV)

    #Método que hace el viewport del archivo.
    def View(self,posX, posY, ancho, alto):
        #En este método se hace el viewport del archivo.
        global Posx, Posy, Ancho, Alto, lista #Instanciando las variables globales del viewport.

        #Llenando las variables globales.
        Posx = posX
        Posy = posY
        Ancho = ancho
        Alto = alto

        #print(Posx, Posy)

        #Probando la lista.
        lista = [
                [colorV for x in range(Ancho)]
                for y in range(Alto)
            ]

        #print("Lista del viewport", lista)

        #Hacer una copia del viewport en el framebuffer con los índices iguales.
        for i in range(Ancho):
            for j in range(Alto):
                self.framebuffer[Posx + i][Posy + j] = lista[i][j]
        
        #print(framebuffer)

        #Hacer un cuadrado en el framebuffer.
        # for x in range(Ancho):
        #     for y in range(Alto):
        #         #print(Posx, Posy)
        #         #print(framebuffer[x][y])
        #         framebuffer[x][y] = colorV

        #print("sss")

        #framebuffer[Posx][Posy] = colorV #El color del viewport es el color actual.


    def Vertex(x, y):
        #En este método se dibuja un punto en el viewport.
        global equis, ye #Instanciando las variables globales de las posiciones del punto.

        #Llenando las variables globales.
        equis = x
        ye = y

        #print(equis, ye)

        #Colocar el punto en el viewport.
        framebuffer[ye][equis] = colorA


        #print("Coordenadas del punto: ", ye, equis)
        #print("Punto: ", framebuffer[ye][equis])

    """
    def Line(x, y):
        #En este método se dibuja una línea en el viewport.
        global equis, ye #Instanciando las variables globales de las posiciones del punto.

        #Llenando las variables globales.
        equis = x
        ye = y

        #print(equis, ye)

        #Colocar el punto en el viewport.
        framebuffer[equis][ye] = colorA


        #print("Coordenadas del punto: ", equis, ye)
        print("Punto: ", framebuffer[equis][ye])
    """
    #Método que escribe el archivo bmp.
    def write(self):
            
            #Se abre el archivo con la forma de bw.
            f = open("SR3.bmp", "bw")

            #Se escribe el encabezado del archivo.

            #Haciendo el pixel header.
            f.write(char('B'))
            f.write(char('M'))
            #Escribiendo el tamaño del archivo en bytes.
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0)) #Cosa que no se utilizará en este caso.
            f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
            #Lo anterior suma 14 bytes.

            #Información del header.
            f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
            f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
            f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width * self.width * 3)) #Tamaño de la imagen sin el header.
            #Pixels que no se usarán mucho.
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #Lo anterior suma 40 bytes.

            #print("Framebuffer", framebuffer)

            #print(framebuffer[Posx][Posy])

            #Pintando el archivo de color negro.
            # for x in range(altoP):
            #     for y in range(anchoP):
            #         f.write(framebuffer[y][x])

            #Pintando el archivo de color negro.
            for y in range(self.height):
                for x in range(self.width):
                    f.write(self.framebuffer[y][x])

            #print(framebuffer)
            #print("Lista temporal en write", lista)
        
            # framebuffer[Posx][Posy] = lista #El color del punto es el color actual.
            # print("Framebuffer con el viewport cargado", framebuffer)
            #Aquí encima se escribe el cuadrado para meter el punto.
            #View(Posx, Posy, Ancho, Alto)
            #punto(equis, ye) #Aquí se tiene que escribir el punto del archivo.


            f.close() #Cerrando el archivo que se escribió.