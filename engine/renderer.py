import glfw.GLFW as GLFW
import OpenGL.GL as GL
import numpy as NUMPY

width, height = None, None


def render(window):
    GL.glViewport(0, 0, width, height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    vao = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(vao)

    vertices = NUMPY.array([
        -0.5, -0.5, 0.0,
        0.5, -0.5, 0.0,
        0.0,  0.5, 0.0], NUMPY.float32)
    vbo = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL.GL_STATIC_DRAW)

    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
    GL.glEnableVertexAttribArray(0)

    vert_shader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
    GL.glShaderSource(vert_shader, open("./gui.vert", "r").read())
    GL.glCompileShader(vert_shader)

    frag_shader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
    GL.glShaderSource(frag_shader, open("./gui.frag", "r").read())
    GL.glCompileShader(frag_shader)

    shader_program = GL.glCreateProgram()

    GL.glAttachShader(shader_program, vert_shader)
    GL.glAttachShader(shader_program, frag_shader)

    GL.glLinkProgram(shader_program)
    GL.glUseProgram(shader_program)

    GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

    GL.glDeleteShader(vert_shader)
    GL.glDeleteShader(frag_shader)
    GL.glBindVertexArray(0)

    GLFW.glfwSwapBuffers(window)
    GLFW.glfwPollEvents()
