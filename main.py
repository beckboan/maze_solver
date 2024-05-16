from graphics import Window, Line, Point
from grid import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    m = Maze(Point(50, 50), 10, 12, 50, 50, win)

    m.solve()

    win.wait_for_close()


main()
