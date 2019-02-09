import OpenGL.GL as GL
import numpy as NUMPY


class Buffer:
    def __init__(self, buffer_type):
        self.__bufferObj = GL.glGenBuffers(1)
        self.__buffer_type = buffer_type

    def bind(self):
        GL.glBindBuffer(self.__buffer_type, self.__bufferObj)

    def unbind(self):
        GL.glBindBuffer(self.__buffer_type, 0)

    def bufferData(self, data):
        GL.glBufferData(self.__buffer_type, data.nbytes, data, GL.GL_DYNAMIC_DRAW)


class VertexBuffer:
    def __init__(self):
        self.__buffer = Buffer(GL.GL_ARRAY_BUFFER)
        self.__vertices = Vertices()

    def buildVBO(self, attr):
        self.__buffer.bind()
        print(attr.getVertices())
        self.__buffer.bufferData(attr.getVertices())
        attr.build()
        self.__buffer.unbind()

    def getBuffer(self):
        return self.__buffer


class VertexArray:
    def __init__(self):
        self.__arrayObj = GL.glGenVertexArrays(1)
        self.__vbo = VertexBuffer()
        self.__textures = []
        self.__tex_coord = []

    def buildVAO(self, attr):
        GL.glBindVertexArray(self.__arrayObj)
        self.__vbo.buildVBO(attr.attr(self.__tex_coord, 2))
        GL.glBindVertexArray(0)

    def getVAO(self):
        return self.__arrayObj

    def useVAO(self, program):
        GL.glBindVertexArray(self.__arrayObj)

        if self.__tex_coord:
            for texture in self.__textures:
                texture.activeAsGLTexture(self.__textures.index(texture))
                program.setInt(texture.getUniform(), self.__textures.index(texture))

    def unBind(self):
        GL.glBindVertexArray(0)
        if self.__tex_coord:
            GL.glBindTexture(GL.GL_TEXTURE_2D, 0)

    def attachTexture(self, texture):
        self.__textures.append(texture)

    def texCoord(self, tex_coord):
        self.__tex_coord = tex_coord
        return self


glFloatSize = GL.ctypes.sizeof(GL.ctypes.c_float)


class Vertices:
    def __init__(self):
        self.__vertices = []
        self.__args = []
        self.stride = 0
        self.offset = 0
        self.count = 0

    def attr(self, attr, n):
        index = 0
        num = 0
        self.stride += n

        for data in attr:
            if num >= n:
                num = 0
                index += self.stride

            self.__vertices.insert(self.offset + index + num, data)

            num += 1

        self.__args.append((
            self.count,
            n,
            GL.GL_FLOAT,
            GL.GL_FALSE,
            None,
            GL.ctypes.c_void_p(self.offset * glFloatSize)
        ))

        self.offset += n
        self.count += 1

        return self

    def build(self):
        for arg in self.__args:
            print(arg)
            GL.glVertexAttribPointer(arg[0], arg[1], arg[2], arg[3], self.stride * glFloatSize, arg[5])
            GL.glEnableVertexAttribArray(arg[0])

    def getVertices(self):
        return NUMPY.array(self.__vertices, NUMPY.float32)

