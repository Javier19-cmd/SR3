#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from Obj import * #Importando los métodos del archivo Obj.py

def main():
    Object('Jeep.obj') #Llamando al método Object del archivo Obj.py.
    scale = (3, 3)
    translate = (512, 512)
    pintar(scale, translate)

main()