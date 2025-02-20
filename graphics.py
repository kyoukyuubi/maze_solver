from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_first, point_second):
        self.first_point = point_first
        self.second_point = point_second

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y, fill=fill_color, width=2
        )
