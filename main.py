from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(50, 50, 100, 100, win)
    cell.has_top_wall = False
    cell.has_right_wall = False
    cell.draw()
    win.wait_for_close()

main()