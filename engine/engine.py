import glfw.GLFW as GLFW
import OpenGL.GL as GL
import numpy as NUMPY

from engine import keyBinding, renderer


def initialize(window):
    keyBinding.keyBindings.append(keyBinding.KeyBinding(GLFW.GLFW_KEY_S))

    renderer.width = window.width
    renderer.height = window.height


def errorCallback(error, description):
    raise RuntimeWarning("Error:" + "Error Code: " + error + " " + "Description: " + description)


def keyCallBack(window, key, scancode, action, mods):
    keyBinding.keyCallback(key, action)


def sizeCallback(window, width, height):
    renderer.width = width
    renderer.height = height


def loopCallback(window):
    if keyBinding.pressed(GLFW.GLFW_KEY_S):
        print("Test")
        pass

    renderer.render(window)
