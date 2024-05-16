from grid import Cell
from graphics import Point
import time
import random


class Maze:
    def __init__(self, rows, cols, size_x, size_y, win=None, seed=None):
        # Check for Exceptions first

        if rows < 1 or cols < 1:
            raise ValueError("Rows and Columns must be greater than 0")

        self.sp = 0
        if win is None:
            self.sp = Point(0, 0)
        else:
            total_width = cols * size_x
            total_height = rows * size_y
            self.sp = Point((win._width - total_width)/2,
                            (win._height - total_height)/2)

        self.rows = rows
        self.cols = cols
        self.size_x = size_x
        self.size_y = size_y
        self._win = win
        self._cells = []
        self._animate_time = 0.01

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
        # print("NEW \n")

        cur_cell = self._cells[i][j]
        cur_cell._visited = True

        if i == self.rows - 1 and j == self.cols - 1:
            return True

        # Find possible cells
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        possible_cells = []

        for x in range(0, len(cur_cell.walls)):
            dir = cur_cell.walls[x]
            # print(f"Wall Num {x} - Direction {dir}")
            if dir == 0:
                ni = i + directions[x][0]
                nj = j + directions[x][1]

                # print(f"New Coords ni = {ni}, nj = {nj}")
                if 0 <= ni < self.rows and 0 <= nj < self.cols and not self._cells[ni][nj]._visited:
                    possible_cells.append((ni, nj))

        if not possible_cells:
            return False

        for ni, nj in possible_cells:
            self._cells[i][j].draw_move(self._cells[ni][nj])
            if self._solve_r(ni, nj):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[ni][nj], True)

        return False

    def solve(self):
        return self._solve_r(0, 0)
