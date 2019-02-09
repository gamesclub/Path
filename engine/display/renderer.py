import glfw.GLFW as GLFW
import OpenGL.GL as GL
import numpy as NUMPY
import glm as GLM

from engine.display.shader import ShaderProgram
from engine.display.buffers import VertexArray, Vertices
from engine.display.texture import Texture


def setupRenderer():
    global program, vao, indices, cube_positions

    shader_program = ShaderProgram("ui").buildProgram()

    indices = NUMPY.array([0, 1, 3,
                           1, 2, 3], NUMPY.int32)

    cube_positions = [
        GLM.vec3(0.0,  0.0,  0.0),
        GLM.vec3(2.0,  5.0, -15.0),
        GLM.vec3(-1.5, -2.2, -2.5),
        GLM.vec3(-3.8, -2.0, -12.3),
        GLM.vec3(2.4, -0.4, -3.5),
        GLM.vec3(-1.7,  3.0, -7.5),
        GLM.vec3(1.3, -2.0, -2.5),
        GLM.vec3(1.5,  2.0, -2.5),
        GLM.vec3(1.5,  0.2, -1.5),
        GLM.vec3(-1.3,  1.0, -1.5)
    ]

    vao = VertexArray().texCoord([
        0.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,

        0.0, 0.0,
        1.0, 0.0,
        1.0, 1.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,

        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,
        1.0, 0.0,

        1.0, 0.0,
        1.0, 1.0,
        0.0, 1.0,
        0.0, 1.0,
        0.0, 0.0,
        1.0, 0.0,

        0.0, 1.0,
        1.0, 1.0,
        1.0, 0.0,
        1.0, 0.0,
        0.0, 0.0,
        0.0, 1.0,

        0.0, 1.0,
        1.0, 1.0,
        1.0, 0.0,
        1.0, 0.0,
        0.0, 0.0,
        0.0, 1.0
    ])

    vao.attachTexture(Texture("uiTexture").attachTexture("./TEST.png"))
    vao.attachTexture(Texture("uiTextureFace").attachTexture("./awesomeface.png"))

    vao.buildVAO(
        Vertices().attr([
            -0.5, -0.5, -0.5,
            0.5, -0.5, -0.5,
            0.5, 0.5, -0.5,
            0.5, 0.5, -0.5,
            -0.5, 0.5, -0.5,
            -0.5, -0.5, -0.5,

            -0.5, -0.5, 0.5,
            0.5, -0.5, 0.5,
            0.5, 0.5, 0.5,
            0.5, 0.5, 0.5,
            -0.5, 0.5, 0.5,
            -0.5, -0.5, 0.5,

            -0.5, 0.5, 0.5,
            -0.5, 0.5, -0.5,
            -0.5, -0.5, -0.5,
            -0.5, -0.5, -0.5,
            -0.5, -0.5, 0.5,
            -0.5, 0.5, 0.5,

            0.5, 0.5, 0.5,
            0.5, 0.5, -0.5,
            0.5, -0.5, -0.5,
            0.5, -0.5, -0.5,
            0.5, -0.5, 0.5,
            0.5, 0.5, 0.5,

            -0.5, -0.5, -0.5,
            0.5, -0.5, -0.5,
            0.5, -0.5, 0.5,
            0.5, -0.5, 0.5,
            -0.5, -0.5, 0.5,
            -0.5, -0.5, -0.5,

            -0.5, 0.5, -0.5,
            0.5, 0.5, -0.5,
            0.5, 0.5, 0.5,
            0.5, 0.5, 0.5,
            -0.5, 0.5, 0.5,
            -0.5, 0.5, -0.5
        ], 3)
    )

    program = shader_program

    vao = vao
    indices = indices

    GL.glEnableClientState(GL.GL_VERTEX_ARRAY)
    GL.glEnable(GL.GL_DEPTH_TEST)


def render(window):
    global program, vao, indices, cube_positions

    GLFW.glfwPollEvents()

    GL.glViewport(0, 0, window.width, window.height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    program.useProgram()

    view = GLM.mat4(1.0)
    view = GLM.translate(view, GLM.vec3(0.0, 0.0, -3.0))

    projection = GLM.perspective(GLM.radians(45.0), window.width / window.height, 0.1, 100.0)

    program.setMat4("view", view)
    program.setMat4("projection", projection)

    for w in range(10):
        model = GLM.mat4(1.0)
        model = GLM.translate(model, cube_positions[w])
        model = GLM.rotate(model, GLM.radians(20.0 * w), GLM.vec3(1.0, 0.3, 0.5))
        program.setMat4("model", model)
        vao.useVAO(program)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 36)

    vao.unBind()

    GLFW.glfwSwapBuffers(window.getWindow())
