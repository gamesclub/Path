import glfw.GLFW as GLFW


class KeyBinding:
    key, state, pressed = None, GLFW.GLFW_RELEASE, False

    def __init__(self, key):
        self.key = key


keyBindings = []


def keyCallback(key, action):
    for keyBinding in keyBindings:
        if keyBinding.key == key:
            keyBinding.state = action


def pressed(key):
    for keyBinding in keyBindings:
        if keyBinding.key == key and (keyBinding.state == GLFW.GLFW_PRESS or keyBinding.state == GLFW.GLFW_REPEAT):
            return True
    return False
