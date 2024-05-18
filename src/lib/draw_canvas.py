from pynput import mouse
from pynput import keyboard
from time import sleep
import lib.select_point as sp
import lib.select_color as sc

TIME_SLEEP = 0.1

# Draw a pixel
def draw_pixel(mouse_controller : mouse.Controller, pos : tuple[int,int]) -> None:
    mouse_controller.position = pos
    mouse_controller.click(mouse.Button.left)
    sleep(TIME_SLEEP)

# Draw the image pixel by pixel
def draw_image(mouse_controller : mouse.Controller, canvas_points, image_color : list[list[tuple[int,int,int]]]) -> None:
    # Get the size of the image
    size = len(image_color)

    # Keyboard listener to stop the drawing
    def on_press(key):
        if key.char == 'm':
            listener.stop()
            return False
        
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Get the vector of the canvas
    vector_x = sp.vector(canvas_points['canvas_upper_left'], canvas_points['canvas_upper_right'])
    vector_y = sp.vector(canvas_points['canvas_upper_left'], canvas_points['canvas_lower_left'])

    for i in range(size):
        for j in range(size):
            # Calculate the position of the pixel
            pos = sp.map_point(canvas_points['canvas_upper_left'], vector_x, vector_y, (i / (size - 1), j / (size - 1)))

            # Change the color of the pixel
            sc.change_color(mouse_controller, image_color[j][i], canvas_points) # Invert i and j because the image is in the wrong direction

            # Draw the pixel
            draw_pixel(mouse_controller, pos)

            # Stop the drawing if the key 'm' is pressed
            if not listener.running:
                return

# Draw image color by color
def draw_image_color(mouse_controller : mouse.Controller, canvas_points, image_color : list[list[tuple[int,int,int]]]) -> None:
    # Get the size of the image
    size = len(image_color)

    # Keyboard listener to stop the drawing
    def on_press(key):
        if key.char == 'm':
            listener.stop()
            return False
        
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Get the vector of the canvas
    vector_x = sp.vector(canvas_points['canvas_upper_left'], canvas_points['canvas_upper_right'])
    vector_y = sp.vector(canvas_points['canvas_upper_left'], canvas_points['canvas_lower_left'])

    pixels_by_color = {}
    for i in range(size):
        for j in range(size):
            color = image_color[j][i]

            if color not in pixels_by_color:
                pixels_by_color[color] = []

            pixels_by_color[color].append((i, j))

    for color in pixels_by_color:
        # Change the color of the pixel
        sc.change_color(mouse_controller, color, canvas_points)

        for pixel in pixels_by_color[color]:
            # Calculate the position of the pixel
            pos = sp.map_point(canvas_points['canvas_upper_left'], vector_x, vector_y, (pixel[0] / (size - 1), pixel[1] / (size - 1)))

            # Draw the pixel
            draw_pixel(mouse_controller, pos)

            # Stop the drawing if the key 'm' is pressed
            if not listener.running:
                return