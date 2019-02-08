import glfw.GLFW as GLFW


class Window:
    __window, __loop, __initialize = None, None, None

    width, height = 600, 600

    def __init__(self):
        if not GLFW.glfwInit():
            raise EnvironmentError("Could not initialize the library.")

        self.__window = GLFW.glfwCreateWindow(self.width, self.height, "Path", None, None)

        if not self.__window:
            GLFW.glfwTerminate()
            raise RuntimeError("Could create a window.")

    def initialize(self, engine):
        GLFW.glfwSetErrorCallback(engine.errorCallback)
        GLFW.glfwSetWindowSizeCallback(self.__window, self.sizeCallback)
        self.windowHint()
        self.__loop = engine.loopCallback
        self.__initialize = engine.initialize

    def windowHint(self):
        GLFW.glfwWindowHint(GLFW.GLFW_OPENGL_FORWARD_COMPAT, True)
        GLFW.glfwWindowHint(GLFW.GLFW_OPENGL_PROFILE, GLFW.GLFW_OPENGL_CORE_PROFILE)

        GLFW.glfwWindowHint(GLFW.GLFW_CONTEXT_VERSION_MAJOR, 2)
        GLFW.glfwWindowHint(GLFW.GLFW_CONTEXT_VERSION_MINOR, 1)

    def showWindow(self):
        GLFW.glfwMakeContextCurrent(self.__window)
        self.__initialize()

        while not GLFW.glfwWindowShouldClose(self.__window):
            self.__loop(self)

        GLFW.glfwTerminate()

    def sizeCallback(self, unused_window, width, height):
        self.width = width
        self.height = height

    def getWindow(self):
        return self.__window
