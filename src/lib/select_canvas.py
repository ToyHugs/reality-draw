from pynput import mouse
from pynput import keyboard

class Canvas:
    def __init__(self):
        self.mouses = mouse.Controller()
        self.keys_listener = keyboard.Listener(on_press=self.on_press)
        self.keys_listener.start()

        # list of point (x, y) when mouse click
        self.R_max = None
        self.R_min = None
        self.G_max = None
        self.G_min = None
        self.B_max = None
        self.B_min = None
        self.change_color_point_plus = None
        self.change_color_point_cross = None
        self.canvas_upper_left = None
        self.canvas_lower_left = None
        self.canvas_upper_right = None

        
    def on_press(self, key):
        try:
            if key.char == 'r':
                self.R_max = self.mouses.position
            elif key.char == 'e':
                self.R_min = self.mouses.position
            elif key.char == 'g':
                self.G_max = self.mouses.position
            elif key.char == 'f':
                self.G_min = self.mouses.position
            elif key.char == 'b':
                self.B_max = self.mouses.position
            elif key.char == 'v':
                self.B_min = self.mouses.position
            elif key.char == 'p':
                self.change_color_point_plus = self.mouses.position
            elif key.char == 'c':
                self.change_color_point_cross = self.mouses.position
            elif key.char == 'u':
                self.canvas_upper_left = self.mouses.position
            elif key.char == 'j':
                self.canvas_lower_left = self.mouses.position
            elif key.char == 'i':
                self.canvas_upper_right = self.mouses.position
        except AttributeError:
            pass

    def print_points(self):
        print(f'R_max: {self.R_max}')
        print(f'R_min: {self.R_min}')
        print(f'G_max: {self.G_max}')
        print(f'G_min: {self.G_min}')
        print(f'B_max: {self.B_max}')
        print(f'B_min: {self.B_min}')
        print(f'Change color point plus: {self.change_color_point_plus}')
        print(f'Change color point cross: {self.change_color_point_cross}')
        print(f'Canvas upper left: {self.canvas_upper_left}')
        print(f'Canvas lower left: {self.canvas_lower_left}')
        print(f'Canvas upper right: {self.canvas_upper_right}')

    def get_points(self):
        return {
            'R_max': self.R_max,
            'R_min': self.R_min,
            'G_max': self.G_max,
            'G_min': self.G_min,
            'B_max': self.B_max,
            'B_min': self.B_min,
            'change_color_point_plus': self.change_color_point_plus,
            'change_color_point_cross': self.change_color_point_cross,
            'canvas_upper_left': self.canvas_upper_left,
            'canvas_lower_left': self.canvas_lower_left,
            'canvas_upper_right': self.canvas_upper_right
        }
    
    def is_all_points_set(self):
        return self.R_max is not None and self.R_min is not None and self.G_max is not None and self.G_min is not None and self.B_max is not None and self.B_min is not None and self.change_color_point_plus is not None and self.change_color_point_cross is not None and self.canvas_upper_left is not None and self.canvas_lower_left is not None and self.canvas_upper_right is not None
    

    def __del__(self):
        self.keys_listener.stop()