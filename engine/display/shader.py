import OpenGL.GL as GL
import glm as GLM


class Shader:
    def __init__(self, shader_type):
        self.__shaderType = shader_type
        self.__shaderObj = GL.glCreateShader(self.__shaderType)

    def buildShader(self, source):
        suffix = ".vert"
        if self.__shaderType != GL.GL_VERTEX_SHADER:
            suffix = ".frag"

        GL.glShaderSource(self.__shaderObj, open(source + suffix).read())
        GL.glCompileShader(self.__shaderObj)

        success = GL.glGetShaderiv(self.__shaderObj, GL.GL_COMPILE_STATUS)
        if success != GL.GL_TRUE:
            raise RuntimeError(GL.glGetShaderInfoLog(self.__shaderObj))

        return self

    def getShaderObj(self):
        return self.__shaderObj

    def delete(self):
        GL.glDeleteShader(self.__shaderObj)
        del self


class ShaderProgram:
    def __init__(self, label):
        self.__programObj = GL.glCreateProgram()
        self.__vert_shader = Shader(GL.GL_VERTEX_SHADER)
        self.__frag_shader = Shader(GL.GL_FRAGMENT_SHADER)
        self.label = label

    def buildProgram(self):
        self.__vert_shader.buildShader(self.label)
        self.__frag_shader.buildShader(self.label)

        GL.glAttachShader(self.__programObj, self.__vert_shader.getShaderObj())
        GL.glAttachShader(self.__programObj, self.__frag_shader.getShaderObj())

        GL.glLinkProgram(self.__programObj)

        success = GL.glGetProgramiv(self.__programObj, GL.GL_LINK_STATUS)
        if success != GL.GL_TRUE:
            raise RuntimeError(GL.glGetProgramInfoLog(self.__programObj))

        self.__vert_shader.delete()
        self.__frag_shader.delete()

        return self

    def getProgramObj(self):
        return self.__programObj

    def useProgram(self):
        GL.glUseProgram(self.__programObj)

    def setInt(self, name, value):
        GL.glUniform1i(GL.glGetUniformLocation(self.getProgramObj(), name), int(value))

    def setBool(self, name, value):
        GL.glUniform1i(GL.glGetUniformLocation(self.getProgramObj(), name), int(value))

    def setFloat(self, name, value):
        GL.glUniform1f(GL.glGetUniformLocation(self.getProgramObj(), name), float(value))

    def setMat4(self, name, value):
        GL.glUniformMatrix4fv(
            GL.glGetUniformLocation(
                self.getProgramObj(),
                name
            ),
            1,
            GL.GL_FALSE,
            GLM.value_ptr(value)
        )
