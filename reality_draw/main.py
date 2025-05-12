from reality_draw.ui.main_window import MainWindow
import tkinter as tk

class RealityDrawApp(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reality Draw")
        self.root.geometry("800x600")
        self.main_window = MainWindow(self.root)

    def run(self):
        self.root.mainloop()