from engine.window import Window
from engine import engine


def main():
    window = Window()
    window.initialize(engine)
    window.showWindow()


if __name__ == "__main__":
    main()
