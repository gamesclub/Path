import glfw.GLFW as GLFW
import time


class Window:
    __window, __loop = None, None

    width, height = 640, 480

    def __init__(self):
        if not GLFW.glfwInit():
            raise EnvironmentError("Could not initialize the library.")

        self.__window = GLFW.glfwCreateWindow(self.width, self.height, "Path", None, None)

        if not self.__window:
            GLFW.glfwTerminate()
            raise RuntimeError("Could create a window.")

    def callBacks(self, callbacks):
        GLFW.glfwSetErrorCallback(callbacks.errorCallback)
        GLFW.glfwSetKeyCallback(self.__window, callbacks.keyCallBack)
        GLFW.glfwSetWindowSizeCallback(self.__window, callbacks.sizeCallback)
        self.__loop = callbacks.loopCallback

    def hints(self):
        GLFW.glfwWindowHint(GLFW.GLFW_OPENGL_FORWARD_COMPAT, True)
        GLFW.glfwWindowHint(GLFW.GLFW_OPENGL_PROFILE, GLFW.GLFW_OPENGL_CORE_PROFILE)

        GLFW.glfwWindowHint(GLFW.GLFW_CONTEXT_VERSION_MAJOR, 2)
        GLFW.glfwWindowHint(GLFW.GLFW_CONTEXT_VERSION_MINOR, 1)

    def showWindow(self):
        GLFW.glfwMakeContextCurrent(self.__window)

        while not GLFW.glfwWindowShouldClose(self.__window):
            self.__loop(self.__window)
            self.sync(GLFW.glfwGetTime())

        GLFW.glfwTerminate()

    def sync(self, start):
        slot = 1 / 30.0
        end = start + slot

        while GLFW.glfwGetTime() < end:
            time.sleep(1 / 1000.0)
