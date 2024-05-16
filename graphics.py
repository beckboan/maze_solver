from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Title"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # self.__root.geometry()

        self._height = height
        self._width = width
        self.__canvas = Canvas(self.__root, bg="white",
                               height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while (self.is_running):
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y,
                           self.end.x, self.end.y, fill=fill_color, width=2)
