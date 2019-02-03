import glfw.GLFW as GLFW
import OpenGL.GL as GL

width, height = None, None


def render(window):
    GL.glViewport(0, 0, width, height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

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

    GL.glDeleteShader(vert_shader)
    GL.glDeleteShader(frag_shader)

    GLFW.glfwSwapBuffers(window)
    GLFW.glfwPollEvents()
