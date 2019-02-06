from engine import renderer


def initialize(window):
    renderer.setupRenderer()


def errorCallback(error, description):
    raise RuntimeWarning("Error:" + "Error Code: " + error + " " + "Description: " + description)


def loopCallback(window):
    renderer.render(window)
