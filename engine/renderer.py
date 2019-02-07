import glfw.GLFW as GLFW
import OpenGL.GL as GL
import numpy as NUMPY
import cv2 as CV

from engine.shader import ShaderProgram
from engine.buffers import VertexArray, Vertices


def setupRenderer():
    global program, vao, indices

    shader_program = ShaderProgram("ui").buildProgram()

    indices = NUMPY.array([0, 1, 3,
                           1, 2, 3], NUMPY.int32)

    texture = GL.glGenTextures(1)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture)

    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_MIRRORED_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_MIRRORED_REPEAT)

    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR_MIPMAP_LINEAR)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

    image = CV.imread("./TEST.png")

    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, image.shape[0], image.shape[1], 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE, image)
    GL.glGenerateMipmap(GL.GL_TEXTURE_2D)

    vao = VertexArray()
    vao.buildVAO(
        Vertices().attr([
            0.5, 0.5,
            0.5, -0.5,
            -0.5, -0.5,
            -0.5, 0.5,
        ], 2).attr([
            1.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0,
            1.0, 1.0, 0.0
        ], 3).attr([
            1.0, 1.0,
            1.0, 0.0,
            0.0, 0.0,
            0.0, 1.0
        ], 2)
    )

    program = shader_program.getProgramObj()
    vao = vao.getVAO()
    indices = indices

    GL.glEnableClientState(GL.GL_VERTEX_ARRAY)


def render(window):
    global program, vao, indices

    GLFW.glfwPollEvents()

    GL.glViewport(0, 0, window.width, window.height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glUseProgram(program)
    GL.glBindVertexArray(vao)
    GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, indices)
    GL.glBindVertexArray(0)

    GLFW.glfwSwapBuffers(window.getWindow())
