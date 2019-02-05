import glfw.GLFW as GLFW
import OpenGL.GL as GL

from engine import renderer


def initialize(window):
    renderer.width = window.width
    renderer.height = window.height


def errorCallback(error, description):
    raise RuntimeWarning("Error:" + "Error Code: " + error + " " + "Description: " + description)


def sizeCallback(window, width, height):
    renderer.width = width
    renderer.height = height
    GL.glViewport(0, 0, width, height)


def loopCallback(window):
    renderer.render(window)


def setupRenderer():
    GL.glViewport(0, 0, renderer.width, renderer.height)

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

    GL.glDeleteShader(vert_shader)
    GL.glDeleteShader(frag_shader)

    vertices = GL.arrays.GLfloatArray.asArray([0.5, 0.5, 0.0,
                                               0.5, -0.5, 0.0,
                                               -0.5, -0.5, 0.0,
                                               -0.5, 0.5, 0.0])

    indices = GL.arrays.GLuintArray.asArray([0, 1, 3,
                                             1, 2, 3])

    vao = GL.glGenVertexArrays(1)
    vbo = GL.glGenBuffers(1)
    ibo = GL.glGenBuffers(1)

    GL.glBindVertexArray(vao)

    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, GL.arrays.GLfloatArray.arraySize(vertices), vertices, GL.GL_STATIC_DRAW)

    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, ibo)
    GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, GL.arrays.GLuintArray.arraySize(indices), indices, GL.GL_STATIC_DRAW)

    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
    GL.glEnableVertexAttribArray(0)

    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
    GL.glBindVertexArray(0)

    renderer.program = shader_program
    renderer.vao = vao

    GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)
    GL.glEnableClientState(GL.GL_VERTEX_ARRAY)
