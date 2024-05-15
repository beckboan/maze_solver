from graphics import Line, Point


class Cell:
    def __init__(self, win):

        self._p1 = None
        self._p2 = None
        self.walls = [1, 1, 1, 1]  # Wall presence (starting top, going CW)
        self._win = win

    def draw(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
        line1 = Line(p1, Point(p2.x, p1.y))
        line2 = Line(Point(p2.x, p1.y), p2)
        line3 = Line(p2, Point(p1.x, p2.y))
        line4 = Line(Point(p1.x, p2.y), p1)

        if self.walls[0] == 1:
            self._win.draw_line(line1)
        else:
            self._win.draw_line(line1, "white")

        if self.walls[1] == 1:
            self._win.draw_line(line2)
        else:
            self._win.draw_line(line2, "white")

        if self.walls[2] == 1:
            self._win.draw_line(line3)
        else:
            self._win.draw_line(line3, "white")

        if self.walls[3] == 1:
            self._win.draw_line(line4)
        else:
            self._win.draw_line(line4, "white")

    def draw_move(self, to_cell, undo=False):
        line_color = "gray"
        if not undo:
            line_color = "red"

        center1 = Point((self._p1.x + self._p2.x)//2,
                        (self._p1.y + self._p2.y)//2)

        center2 = Point((to_cell._p1.x + to_cell._p2.x)//2,
                        (to_cell._p1.y + to_cell._p2.y)//2)

        line = Line(center1, center2)
        self._win.draw_line(line, line_color)
