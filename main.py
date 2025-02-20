from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    first_point = Point(0, 0)
    second_point = Point(800, 600)
    first_line = Line(first_point, second_point)
    win.draw_line(first_line, "blue")
    win.draw_line(
        Line(
            Point(50, 300), Point(500, 300)
        ),
        "red"
    )
    win.draw_line(Line(Point(500, 100), Point(500, 400)), "yellow")
    win.wait_for_close()

main()