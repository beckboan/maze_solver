from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.widget = Tk()
        self.widget.title = "Title"

        self.canvas = Canvas()
        self.canvas.pack()

        self.is_running = False

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()

    def wait_for_close(self):
        self.is_running = True
        while (self.is_running):
            self.redraw()
