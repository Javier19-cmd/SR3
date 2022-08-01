"""
Referencias: 
1. Arreglar el ValueError: could not convert string to float: 
    https://researchdatapod.com/python-valueerror-could-not-convert-string-to-float/
2. Try except para los obj's que tienen doble /: 
    https://bobbyhadz.com/blog/python-valueerror-invalid-literal-for-int-with-base-10
"""
lines = [] #Lista que guarda las líneas del archivo que lee.
faces = [] #Lista que guarda las caras de la imagen.
vertices = [] #Lista que guarda los vértices de la imagen.

from gl import * #Importando el archivo gl.py, que tiene el método para escribir la línea en el framebuffer.

def Object(filename):
    """
    Variables globales: 
        1. lines: Lista que guarda las líneas del archivo que lee.
        2. faces: Lista que guarda las caras de la imagen.
        3. vertices: Lista que guarda los vértices de la imagen. 
    """
    global lines, faces, vertices
    
    with open(filename) as f: #Abriendo el archivo .obj.
        lines = f.read().splitlines() #Se leen las líneas, se hacen split y se guardan en la variable global lines.

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
        if prefix == 'f': #Si el prefijo es f, se agrega el valor a la lista de caras.
            try: 
                faces.append(
                    [
                        list(
                            map(int, face.strip().split('/') #Se quita el / y se convierte a entero.
                            )
                        ) 
                        for face in value.strip().split(' ') #Se quita el espacio.
                    ]
                )
            except: #Aquí se quitan las caras que tienen doble /.
                faces.append(
                    [
                        list(
                            map(int, face.strip().split('//') #Se quita el / y se convierte a entero.
                            )
                        ) 
                        for face in value.strip().split(' ') #Se quita el espacio.
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

#Función que transforma las caras de la estructura de la imagen.
def pintar(scale, translate):

    print(scale, translate)

    print(len(lines))
    print(len(faces))
    print(len(vertices))

    #Recorriendo las caras e imprimiéndolas.
    for face in faces: 
        #print(face) #Debuggeo.
        
        if len(face) == 4: #Validando que la cara tenga 4 vértices.
            #El array de caras es bidimensional en este código.
            f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][0] - 1 #Agarrando el índice 0.
            f3 = face[2][0] - 1 #Agarrando el índice 1.
            f4 = face[3][0] - 1 #Agarrando el índice 2.

            #Transformando los vértices.
            v1 = transform_vertex(vertices[f1], scale, translate)
            v2 = transform_vertex(vertices[f2], scale, translate)
            v3 = transform_vertex(vertices[f3], scale, translate)
            v4 = transform_vertex(vertices[f4], scale, translate)

            #print("Cara: ", f1, f2, f3, f4)

        elif len(face) == 3: #Validando que la cara tenga 3 vértices.
            f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][0] - 1 #Agarrando el índice 0.
            f3 = face[2][0] - 1 #Agarrando el índice 1.
            #f4 = face[3][0] - 1 #Agarrando el índice 2.

            #Transformando los vértices.
            v1 = transform_vertex(vertices[f1], scale, translate)
            v2 = transform_vertex(vertices[f2], scale, translate)
            v3 = transform_vertex(vertices[f3], scale, translate)

            #print("Cara: ", f1, f2, f3)

            #Vértices 1 y 2.
            glLine(
                v1[0][0], #X del vértice 1.
                v1[0][1], #Y del vértice 1.
                v2[0][0], #X del vértice 2.
                v2[0][1] #Y del vértice 2.
            )

            #Vértices 2 y 3.
            glLine(
                v2[0][0], #X del vértice 2.
                v2[0][1], #Y del vértice 2.
                v3[0][0], #X del vértice 3.
                v3[0][1] #Y del vértice 3.
            )

            #Vértices 3 y 1.
            glLine(
                v3[0][0], #X del vértice 3.
                v3[0][1], #Y del vértice 3.
                v1[0][0], #X del vértice 1.
                v1[0][1] #Y del vértice 1.
            )