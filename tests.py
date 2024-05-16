import unittest

from maze import Maze
from graphics import Point


class Tests(unittest.TestCase):
    def test_column_row(self):
        cols = 10
        rows = 10

        m = Maze(rows, cols, 10, 10)
        self.assertEqual(len(m._cells), cols)
        self.assertEqual(len(m._cells[0]), rows)

    def test_no_col(self):
        cols = 0
        rows = 10

        self.assertRaises(ValueError, Maze, rows, cols, 10, 10)

    def test_no_row(self):
        cols = 10
        rows = 0

        self.assertRaises(ValueError, Maze, rows, cols, 10, 10)

    def test_maze_opening(self):
        cols = 10
        rows = 10

        m = Maze(rows, cols, 10, 10)
        self.assertEqual(m._cells[0][0].walls[0], 0)
        self.assertEqual(m._cells[cols-1][rows-1].walls[2], 0)


if __name__ == "__main__":
    unittest.main()
