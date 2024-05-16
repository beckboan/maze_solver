from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    m = Maze(10, 12, 50, 50, win)

    m.solve()

    win.wait_for_close()


main()
