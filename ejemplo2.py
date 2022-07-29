import struct

def char(c):
    # 1 byte
    return struct.pack('=c',c.encode('ascii'))

def word(w):
    # 2  bytes
    return struct.pack('=h',w)

def dword(d):
    #4 bytes
    return struct.pack('=l', d)

def color (r,g,b):
    return bytes([b,g,r])

BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_color = WHITE
        self.clear()

    def clear(self):
        self.framebuffer = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename):
        f = open(filename, 'bw')

        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

    def point(self, x, y):
        self.framebuffer[x][y] = self.current_color

    def set_current_color(self, c):
        self.current_color = c

    def line(self, x0,y0,x1,y1):
        x0 = round(x0)
        y0 = round(y0)
        x1 = round(x1)
        y1 = round(y1)
        
        dy = abs(y1-y0)
        dx = abs(x1-x0)

        steep = dy > dx

        if steep:
            x0,y0 = y0,x0
            x1,y1 = y1,x1

        if  x0>x1:
            x0,x1 = x1,x0
            y0,y1 = y1,y0

        dy = abs(y1-y0)
        dx = x1-x0

        offset = 0
        threshold = dx
        y = y0

        for x in range(x0,x1 +1):
            if steep:
                self.point(y,x)
            else:
                self.point(x,y)
            offset += dy * 2
            if offset >= threshold:
                y +=1 if y0 < y1 else -1
                threshold += dx * 2

            
class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        
        self.vertices = []
        self.faces = []

        for lines in self.lines:
            prefix, value = lines.split(' ', 1)

            if prefix == 'v':
                self.vertices.append(
                    list(
                        map(float, value.split(' '))
                        )
                    )
            if prefix == 'f':
                self.faces.append([
                    list(map(int, face.split('/'))) 
                        for face in value.split(' ') 
                    ]
                )

def transform_vertex(vertex, scale, translate):
    return [
        (
            (vertex[0] * scale[0]) + translate[0],
            (vertex[1] * scale[1]) + translate[1]
        )
    ]

scale_factor = (5,5)
translate_factor = (150,150)

r = Render(500, 500)
r.set_current_color(color(200,100,0))
cube = Obj('face.obj')

for face in cube.faces:
    if len(face) == 4:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1
        f4 = face[3][0] - 1

        v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor)
        v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor)
        v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor)
        v4 = transform_vertex(cube.vertices[f4], scale_factor, translate_factor)

        r.line(v1[0][0], v1[0][1], v2[0][0], v2[0][1])
        r.line(v2[0][0], v2[0][1], v3[0][0], v3[0][1])
        r.line(v3[0][0], v3[0][1], v4[0][0], v4[0][1])
        r.line(v4[0][0], v4[0][1], v1[0][0], v1[0][1])
    if len(face) == 3:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor)
        v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor)
        v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor)

        r.line(v1[0][0], v1[0][1], v2[0][0], v2[0][1])
        r.line(v2[0][0], v2[0][1], v3[0][0], v3[0][1])
        r.line(v3[0][0], v3[0][1], v4[0][0], v4[0][1])


# square = [
#     (100,100),
#     (200,100),
#     (200,200),
#     (200,200)
# ]

# center = (150,150)

# square_large = [
#     (
#         ((x-center[0]) * 1.5) + center[0],
#         ((y-center[1]) * 3.5) + center[1]
#     )for x, y in square
# ]

#r.line(80,40,13,20)
#r.line(50,50,10,80)
r.write('a.bmp')