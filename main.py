from graphics import Window, Line, Point
from grid import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.walls[1] = 0
    c.draw(Point(50, 50), Point(100, 100))

    c = Cell(win)
    c.walls[3] = 0
    c.draw(Point(100, 100), Point(150, 150))

    win.wait_for_close()


main()
