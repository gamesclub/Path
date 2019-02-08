import glfw.GLFW as GLFW
import OpenGL.GL as GL
import numpy as NUMPY

from engine.display.shader import ShaderProgram
from engine.display.buffers import VertexArray, Vertices
from engine.display.texture import Texture


def setupRenderer():
    global program, vao, indices

    shader_program = ShaderProgram("ui").buildProgram()

    indices = NUMPY.array([0, 1, 3,
                           1, 2, 3], NUMPY.int32)

    vao = VertexArray()

    vao.texCoord([
            1.0, 1.0,
            1.0, 0.0,
            0.0, 0.0,
            0.0, 1.0
        ])

    vao.attachTexture(Texture("uiTexture").attachTexture("./TEST.png"))

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
        ], 3)
    )

    program = shader_program

    vao = vao
    indices = indices

    GL.glEnableClientState(GL.GL_VERTEX_ARRAY)


def render(window):
    global program, vao, indices

    GLFW.glfwPollEvents()

    GL.glViewport(0, 0, window.width, window.height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    vao.useVAO(program)
    GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, indices)
    vao.unBind()

    GLFW.glfwSwapBuffers(window.getWindow())
