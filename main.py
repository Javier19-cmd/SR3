#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from Obj import * #Importando los métodos del archivo Obj.py

def main():
    glCreateWindow(1024, 1024) #Creando la ventana.
    glClearColor(0, 0, 0) #Color del fondo.
    glClear() #Limpiando el framebuffer con el color creado en glClearColor.
    
    #Recibe posición en x,posición en y, ancho, alto.
    glViewPort(312, 400, 301, 301) #Creando el viewport.

    glColor(0.3, 0.4, 0.7) #Asignando el color del punto.

    #glVertex(0.1, 0.3) #Dibujando el punto.
    #glLine(0.1, 0.3, 0.5, 0.5) #Dibujando la línea.
    #glLine(0.1, 0.5, 0.5, 0.3) #Dibujando la línea
    
    # Object('Porsche.obj') #Llamando al método Object del archivo Obj.py.
    # scale = (5, 5)
    # translate = (512, 512)
    # glColor(0.5, 0.3, 0.1)
    # pintar(scale, translate)
    glFinish()

main()