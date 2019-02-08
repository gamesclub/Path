import OpenGL.GL as GL
from PIL import Image
import numpy as NUMPY


class Texture:
    def __init__(self, uniform):
        self.__texture = GL.glGenTextures(1)
        self.__uniform = uniform

        GL.glBindTexture(GL.GL_TEXTURE_2D, self.__texture)

        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_MIRRORED_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_MIRRORED_REPEAT)

        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR_MIPMAP_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

        GL.glBindTexture(GL.GL_TEXTURE_2D, 0)

    def attachTexture(self, img):
        img = Image.open("./TEST.png").transpose(Image.FLIP_TOP_BOTTOM)
        image = NUMPY.array(list(img.getdata()), NUMPY.uint8)

        GL.glBindTexture(GL.GL_TEXTURE_2D, self.__texture)

        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, img.size[0], img.size[1], 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE,
                       image)
        GL.glGenerateMipmap(GL.GL_TEXTURE_2D)

        GL.glBindTexture(GL.GL_TEXTURE_2D, 0)

        return self

    def activeAsGLTexture(self, index):
        GL.glActiveTexture(GL.GL_TEXTURE0 + index)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.__texture)

    def getUniform(self):
        return self.__uniform






