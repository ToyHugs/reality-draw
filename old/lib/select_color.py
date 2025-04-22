from pynput import mouse
from pynput import keyboard
from time import sleep
import lib.select_point as sp

TIME_SLEEP = 0.1

def change_color(mouse_controller : mouse.Controller, rgb : tuple[int,int,int], canvas_points) -> None:
    # Click on the point to change color
    mouse_controller.position = canvas_points['change_color_point_plus']
    mouse_controller.click(mouse.Button.left)
    sleep(TIME_SLEEP)

    # Calculate all the point to click
    red_pos = sp.point_on_segment(canvas_points['R_min'], canvas_points['R_max'], rgb[0] / 255)
    green_pos = sp.point_on_segment(canvas_points['G_min'], canvas_points['G_max'], rgb[1] / 255)
    blue_pos = sp.point_on_segment(canvas_points['B_min'], canvas_points['B_max'], rgb[2] / 255)

    # Click on the red point
    mouse_controller.position = red_pos
    mouse_controller.click(mouse.Button.left)
    sleep(TIME_SLEEP)

    # Click on the green point
    mouse_controller.position = green_pos
    mouse_controller.click(mouse.Button.left)
    sleep(TIME_SLEEP)

    # Click on the blue point
    mouse_controller.position = blue_pos
    mouse_controller.click(mouse.Button.left)
    sleep(TIME_SLEEP)

    # Click on the cross point
    mouse_controller.position = canvas_points['change_color_point_cross']
    mouse_controller.click(mouse.Button.left)
    sleep(TIME_SLEEP)


