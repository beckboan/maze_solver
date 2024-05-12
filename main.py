from graphics import Window, Line, Point
from grid import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    m = Maze(Point(50, 50), 4, 4, 50, 50, win)

    # c1 = Cell(win)
    # c1.walls[1] = 0
    # c1.walls[0] = 0
    # c1.draw(Point(50, 50), Point(100, 100))
    #
    # c2 = Cell(win)
    # c2.walls[3] = 0
    # c2.draw(Point(100, 100), Point(150, 150))
    #
    # c1.draw_move(c2)

    win.wait_for_close()


main()
