from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.has_right_wall = False
    cell1.draw()
    cell2 = Cell(100, 50, 150, 100, win)
    cell2.has_left_wall = False
    cell2.draw()
    cell1.draw_move(cell2, True)
    win.wait_for_close()

main()