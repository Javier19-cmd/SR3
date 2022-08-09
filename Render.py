from utilidades import * #Archivo de utilidades.

class Render(object):

    #Estas variables son globales y tienen valores por defecto y arbitrarios.
    WHITE = color(1, 1, 1) #Color blanco hecho con las utilidades.
    colorFondo = WHITE #Asignando el color blanco al framebuffer.
    #print("Color del fondo: ", colorFondo)
    colorViewPort = WHITE #Asignando el color blanco al viewport. Esto es temporal-
    width = 0 #Ancho de la pantalla. Esto es temporal.
    height = 0 #Alto de la pantalla. Esto es temporal.
    
    widthV = 0 #Ancho del viewport. Esto es temporal.
    heightV = 0 #Alto del viewport. Esto es temporal.

    xV = 0 #Posición en x del viewport.
    yV = 0 #Posición en y del viewport.
    colorP = WHITE #Asignando el color blanco al punto. Esto es temporal.

    #Método que escribe el framebuffer.
    def Framebuffer(self):

        #print(colorP)

        #print(colorP)

        #Llenando de bits el framebuffer.
        self.framebuffer = [
            [self.colorFondo for x in range(self.width)]
            for y in range(self.height)
        ]

        print("Ancho y alto: ", self.width, self.height)
        #print("Framebuffer: ", self.framebuffer)


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


    #Método que hace el viewport del archivo.
    def View(self, posX, posY, ancho, alto):
        #En este método se hace el viewport del archivo.

        #print(Posx, Posy)
        self.xV = posX
        self.yV = posY
        self.widthV = ancho
        self.heightV = alto

        #Probando la lista.
        lista = [
                [self.colorViewPort for x in range(ancho)]
                for y in range(alto)
            ]

        #print("Lista del viewport", lista)

        #Hacer una copia del viewport en el framebuffer con los índices iguales.
        for i in range(ancho):
            for j in range(alto):
                self.framebuffer[posY + j][posX + i] = lista[j][i]
        
        #print(framebuffer)

        #Hacer un cuadrado en el framebuffer.
        # for x in range(Ancho):
        #     for y in range(Alto):
        #         #print(Posx, Posy)
        #         #print(framebuffer[x][y])
        #         framebuffer[x][y] = colorV

        #print("sss")

        #framebuffer[Posx][Posy] = colorV #El color del viewport es el color actual.

    def Vertex(self,x, y):
        #En este método se dibuja un punto en el viewport.
        #global equis, ye #Instanciando las variables globales de las posiciones del punto.


        #print(equis, ye)

        #print(x, y)

        #Colocar el punto en el viewport.
        self.framebuffer[y][x] = self.colorP #El color del punto es el color actual.


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
            f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
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