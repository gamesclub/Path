from engine.window import Window
from engine import engine


def main():
    global window

    window = Window()
    engine.initialize(window)
    window.callBacks(engine)
    window.hints()
    window.showWindow()


if __name__ == "__main__":
    main()
