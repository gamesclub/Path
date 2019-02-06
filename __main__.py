from engine.window import Window
from engine import engine


def main():
    global window

    window = Window()
    window.setup(engine)
    window.showWindow()


if __name__ == "__main__":
    main()
