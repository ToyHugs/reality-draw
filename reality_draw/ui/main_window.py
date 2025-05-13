import tkinter as tk
from tkinter import filedialog  # Import pour la boîte de dialogue de fichier


class MainWindow(object):
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Reality Draw")

        # Create a frame for the main content
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a label for the title
        self.title_label = tk.Label(
            self.main_frame, text="Reality Draw", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        # Create a button to start drawing
        self.draw_button = tk.Button(
            self.main_frame, text="Start Drawing", command=self.start_drawing)
        self.draw_button.pack(pady=10)

        # Create a button to upload an image
        self.upload_button = tk.Button(
            self.main_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

    def start_drawing(self):
        # Placeholder for drawing functionality
        print("Drawing started!")

    def upload_image(self):
        # Ouvrir une boîte de dialogue pour sélectionner un fichier
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg")]
        )
        if file_path:
            print(f"Image selected: {file_path}")
