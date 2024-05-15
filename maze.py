from grid import Cell
from graphics import Point
import time


class Maze:
    def __init__(self, sp, rows, cols, size_x, size_y, win=None):
        # Check for Exceptions first
        if (type(sp) is not Point) or (sp.x < 0 or sp.y < 0):
            raise Exception(
                "Starting point must be of the Point Class and at least (0,0)")

        if rows < 1 or cols < 1:
            raise ValueError("Rows and Columns must be greater than 0")

        self.sp = sp
        self.rows = rows
        self.cols = cols
        self.size_x = size_x
        self.size_y = size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._open_start_end()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for i in range(self.rows)]
                       for j in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.sp.x + i * self.size_x
        y1 = self.sp.y + j * self.size_y

        self._cells[i][j].draw(Point(x1, y1),
                               Point(x1 + self.size_x, y1 + self.size_y))
        self._animate()

    def _open_start_end(self):
        self._cells[0][0].walls[0] = 0
        self._draw_cell(0, 0)
        self._cells[self.cols-1][self.rows-1].walls[2] = 0
        self._draw_cell(self.cols-1, self.rows-1)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
