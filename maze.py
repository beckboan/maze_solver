from grid import Cell
from graphics import Point
import time
import random


class Maze:
    def __init__(self, sp, rows, cols, size_x, size_y, win=None, seed=None):
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
        self._animate_time = 0.1

        if seed:
            random.seed(seed)

        self._create_cells()
        self._open_start_end()
        self._break_walls_r(0, 0)
        self._reset_all_visited()
        # self._solve_r(0, 0)

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self.cols)]
                       for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.sp.x + j * self.size_x
        y1 = self.sp.y + i * self.size_y

        self._cells[i][j].draw(Point(x1, y1),
                               Point(x1 + self.size_x, y1 + self.size_y))
        self._animate()

    def _open_start_end(self):
        self._cells[0][0].walls[0] = 0
        self._draw_cell(0, 0)
        self._cells[self.rows-1][self.cols-1].walls[2] = 0
        self._draw_cell(self.rows-1, self.cols-1)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(self._animate_time)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        # Up, Right, Down, Left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while True:
            adjacent_cells = []
            # Up

            for dc, dr in directions:
                ni, nj = i + dc, j + dr
                if 0 <= ni < self.rows and 0 <= nj < self.cols and not self._cells[ni][nj]._visited:
                    adjacent_cells.append((ni, nj))

            if not adjacent_cells:
                return

            choice = random.randint(0, len(adjacent_cells)-1)
            ni = adjacent_cells[choice][0]
            nj = adjacent_cells[choice][1]

            # print(ni, nj)

            if ni == i-1:
                self._cells[i][j].walls[0] = 0
                self._cells[ni][nj].walls[2] = 0
            elif nj == j+1:
                self._cells[i][j].walls[1] = 0
                self._cells[ni][nj].walls[3] = 0
            elif ni == i+1:
                self._cells[i][j].walls[2] = 0
                self._cells[ni][nj].walls[0] = 0
            elif nj == j-1:
                self._cells[i][j].walls[3] = 0
                self._cells[ni][nj].walls[1] = 0

            self._draw_cell(i, j)

            self._break_walls_r(ni, nj)

    def _reset_all_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

    def _solve_r(self, i, j):
        self._animate()

        return False
