import OpenGL.GL as GL


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
    def __init__(self, vertices, n, indices):
        self.__buffer = Buffer(GL.GL_ARRAY_BUFFER)
        self.__indices = indices
        self.__vertices = vertices
        self.__n = n

    def buildVBO(self):
        self.__buffer.bind()
        self.__buffer.bufferData(self.__vertices)
        # TODO:Add the arrtib operate here
        GL.glVertexAttribPointer(0, self.__n, GL.GL_FLOAT, GL.GL_FALSE, self.__n * GL.ctypes.sizeof(GL.ctypes.c_float), None)
        GL.glEnableVertexAttribArray(0)
        self.__buffer.unbind()

    def getBuffer(self):
        return self.__buffer


class VertexArray:
    def __init__(self):
        self.__arrayObj = GL.glGenVertexArrays(1)

    def buildVAO(self, vbo):
        GL.glBindVertexArray(self.__arrayObj)
        vbo.buildVBO()
        GL.glBindVertexArray(0)

    def getVAO(self):
        return self.__arrayObj
