import glfw.GLFW as GLFW
import OpenGL.GL as GL

width, height = None, None
program, vao = None, None


def render(window):
    global program, vao

    GLFW.glfwPollEvents()

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    GL.glUseProgram(program)

    GL.glBindVertexArray(vao)

    GL.glDrawElements(GL.GL_TRIANGLES, 6, GL.GL_UNSIGNED_INT, 0)

    GL.glBindVertexArray(0)

    GLFW.glfwSwapBuffers(window)
