import time
import glfw.GLFW as GLFW

from engine.display import renderer


def initialize():
    renderer.setupRenderer()


def errorCallback(error, description):
    raise RuntimeWarning("Error:" + "Error Code: " + error + " " + "Description: " + description)


def loopCallback(window):
    renderer.render(window)
    sync(GLFW.glfwGetTime())


def sync(start):
    slot = 1 / 30.0
    end = start + slot

    while GLFW.glfwGetTime() < end:
        time.sleep(1 / 1000.0)
