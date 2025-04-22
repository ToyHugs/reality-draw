# Fichier de test en dessinant un carré, point par point

import sys
import pynput.mouse as mouse
import pynput.keyboard as keyboard
import lib.select_canvas as sc
from time import sleep

def test_draw_square():
    canvas = sc.Canvas()

    is_good = []

    def on_press(key):
        try :
            if key.char == 'p':
                is_good.append(True)
        except AttributeError:
            pass

    keys_listener = keyboard.Listener(on_press=on_press)
    keys_listener.start()

    while not is_good:
        pass
    keys_listener.stop()

    
    canvas.print_points()

    # assert canvas.is_all_points_set()

    mouses = mouse.Controller()

    # Draw square in the middle of the canvas
    vector_unit_x = ((canvas.canvas_upper_right[0] - canvas.canvas_upper_left[0]), (canvas.canvas_upper_right[1] - canvas.canvas_upper_left[1]))
    vector_unit_y = ((canvas.canvas_lower_left[0] - canvas.canvas_upper_left[0]), (canvas.canvas_lower_left[1] - canvas.canvas_upper_left[1]))

    # middle = (vector_unit_x + vector_unit_y) / 2 + canvas.canvas_upper_left
    middle = ((vector_unit_x[0] + vector_unit_y[0])/2 + canvas.canvas_upper_left[0], (vector_unit_x[1] + vector_unit_y[1])/2 + canvas.canvas_upper_left[1])
    # large = (middle - canvas.canvas_upper_left) / 2
    large = ((middle[0] - canvas.canvas_upper_left[0])/2, (middle[1] - canvas.canvas_upper_left[1])/2)

    # mouses.position = middle - large
    mouses.position = (middle[0] - large[0], middle[1] - large[1])
    mouses.press(mouse.Button.left)
    sleep(0.1)
    mouses.position = (middle[0] + large[0], middle[1] - large[1])
    sleep(0.1)
    mouses.release(mouse.Button.left)
    sleep(0.1)
    mouses.position = (middle[0], middle[1])
    mouses.click(mouse.Button.left)
    sleep(0.1)
    n = 150
    for i in range(n+1):
        pos_x = int(canvas.canvas_upper_left[0] + i * (vector_unit_x[0] / n))
        pos_y = int(canvas.canvas_upper_left[1] + i * (vector_unit_x[1] / n))
        mouses.position = (pos_x, pos_y)
        mouses.click(mouse.Button.left)
        sleep(0.10)
    

    print('Test passed')

if __name__ == '__main__':

    test_draw_square()
    sys.exit(0)

