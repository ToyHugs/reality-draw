import tkinter as tk
from reality_draw.core.calculator import add_numbers

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemple Tkinter App")
        self.root.geometry("300x150")

        self.entry1 = tk.Entry(root)
        self.entry2 = tk.Entry(root)
        self.result_label = tk.Label(root, text="Résultat: ")

        self.entry1.pack(pady=5)
        self.entry2.pack(pady=5)

        self.calc_button = tk.Button(root, text="Additionner", command=self.calculate)
        self.calc_button.pack(pady=5)
        self.result_label.pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = add_numbers(num1, num2)
            self.result_label.config(text=f"Résultat: {result}")
        except ValueError:
            self.result_label.config(text="Entrée invalide")
