import glfw.GLFW as GLFW
import OpenGL.GL as GL

width, height = None, None


def render(window):
    GL.glViewport(0, 0, width, height)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    GLFW.glfwSwapBuffers(window)
    GLFW.glfwPollEvents()
