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
        if self.walls[0] == 1:
            line = Line(p1, Point(p2.x, p1.y))
            self._win.draw_line(line)
        if self.walls[1] == 1:
            line = Line(Point(p2.x, p1.y), p2)
            self._win.draw_line(line)
        if self.walls[2] == 1:
            line = Line(p2, Point(p1.x, p2.y))
            self._win.draw_line(line)
        if self.walls[3] == 1:
            line = Line(Point(p1.x, p2.y), p1)
            self._win.draw_line(line)
