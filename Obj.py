"""
Referencias: 
1. Arreglar el ValueError: could not convert string to float: 
    https://researchdatapod.com/python-valueerror-could-not-convert-string-to-float/
"""
lines = []

def Object(filename):
    global lines #Variable global para llenarla con las lineas del archivo.
    
    with open(filename) as f: #Abriendo el archivo .obj.
        lines = f.read().splitlines() #Se leen las líneas, se hacen split y se guardan en la variable global lines.

    #Creando listas para los vértices y las caras.
    vertices = [] #Matriz de los vértices.
    faces = [] #Matriz para las caras.

    for line in lines:

        if not line or line.startswith("#"): #Si hay una línea vacía o una línea que tenga #, se salta. 
            continue

        
        prefix, value = line.split(' ', 1) #Se hace split de la línea en dos partes, el prefijo y el valor.

        if prefix == 'v': #Si el prefijo es v, se agrega el valor a la lista de vértices.
            vertices.append(
                list(
                    map(
                        float, value.strip().split(' ') #Se quitan los strings inválidos y los espacios. Luego se convierten a float.
                    )
                )
            )
            #print(vertices) #Debuggeo.
        else: 
            continue
        if prefix == 'f': #Si el prefijo es f, se agrega el valor a la lista de caras.
            faces.append(
                [
                    list(
                        map(int, face.strip().split('/') #Se quita el / y se convierte a entero.
                        )
                    ) 
                    for face in value.split(' ') #Se quita el espacio.
                ]
            )

#Función que transforma los vértices de la estructura de la imagen.
def transform_vertex(vertex, scale, translate): 
    
    return [
        (
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1] #Y.
        )
    ]