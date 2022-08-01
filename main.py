#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from Obj import * #Importando los métodos del archivo Obj.py

def main():
    glCreateWindow(1024, 1024) #Creando la ventana.
    glClearColor(0.5, 0.5, 0.5) #Color del fondo.
    glClear() #Limpiando el framebuffer.
    Object('Porsche.obj') #Llamando al método Object del archivo Obj.py.
    scale = (5, 5)
    translate = (512, 512)
    glColor(0.5, 0.3, 0.1)
    pintar(scale, translate)
    glFinish()

main()