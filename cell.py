from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Left Wall
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(x1, y1), Point(x1, y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(x1, y1), Point(x1, y2)), "#d9d9d9"
            )

        # Top Wall
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(x1, y1), Point(x2, y1)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(x1, y1), Point(x2, y1)), "#d9d9d9"
            )

        # Right Wall
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(x2, y1), Point(x2, y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(x2, y1), Point(x2, y2)), "#d9d9d9"
            )

        # Bottom Wall
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(x1, y2), Point(x2, y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(x1, y2), Point(x2, y2)), "#d9d9d9"
            )

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"
        
        self_middle_x = (self._x1 - (self._x1 - self._x2) // 2)
        self_middle_y = (self._y1 - (self._y1 - self._y2) // 2)
        to_middle_x = (to_cell._x1 - (to_cell._x1 - to_cell._x2) // 2)
        to_middle_y = (to_cell._y1 - (to_cell._y1 - to_cell._y2) // 2)

        self_point = Point(self_middle_x, self_middle_y)
        to_point = Point(to_middle_x, to_middle_y)

        self._win.draw_line(
            Line(self_point, to_point), color
        )