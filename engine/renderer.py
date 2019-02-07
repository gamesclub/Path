import glfw.GLFW as GLFW
import OpenGL.GL as GL
import numpy as NUMPY

from engine.shader import ShaderProgram
from engine.buffers import VertexArray, Vertices


def setupRenderer():
    global program, vao, indices

    shader_program = ShaderProgram("ui").buildProgram()

    indices = NUMPY.array([0, 1, 2], NUMPY.int32)

    vao = VertexArray()
    vao.buildVAO(
        Vertices().attr([-0.5, -0.5, 0.0, 0.5, -0.5, 0.0, 0.0, 0.5, 0.0], 3).attr([1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], 3)
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
    GL.glDrawElements(GL.GL_TRIANGLES, 3, GL.GL_UNSIGNED_INT, indices)
    GL.glBindVertexArray(0)

    GLFW.glfwSwapBuffers(window.getWindow())
