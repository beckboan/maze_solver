import unittest

from maze import Maze
from graphics import Point


class Tests(unittest.TestCase):
    def test_column_row(self):
        cols = 10
        rows = 10

        m = Maze(Point(0, 0), rows, cols, 10, 10)
        self.assertEqual(len(m._cells), cols)
        self.assertEqual(len(m._cells[0]), rows)

    def test_no_col(self):
        cols = 0
        rows = 10

        self.assertRaises(ValueError, Maze, Point(0, 0), rows, cols, 10, 10)

    def test_no_row(self):
        cols = 10
        rows = 0

        self.assertRaises(ValueError, Maze, Point(0, 0), rows, cols, 10, 10)

    def test_invalid_sp(self):

        self.assertRaises(Exception, Maze, 255, 10, 10, 10, 10)


if __name__ == "__main__":
    unittest.main()
