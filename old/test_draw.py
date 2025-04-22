import lib.draw_canvas as dc
import lib.select_canvas as sc
import lib.img_import as ii

path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\BNA_PP.png"
path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\Instagram_icon.png"
path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\gojo.jpg"

number_of_colors = 500
width = 100
# 50 for big size pen
# 100 for middle size pen
# 200 for small size pen

# Import the image and decomplexify the color of the image
pixels = ii.import_image(path_img)
pixels = ii.resize_image(pixels, width)
pixels = ii.color_reductor(pixels, number_of_colors)

# Show time to draw the canvas
time_to_draw = width * width * 0.1 + number_of_colors * 0.5
print(f"Time estimate to draw the canvas: {time_to_draw//60} minutes and {time_to_draw%60} seconds")

# Create the canvas
canvas = sc.Canvas()

# Ask the user to draw the canvas, then print the points
print("Draw the canvas by press touch on the keyboard on the following points:")
print("r: R_max")
print("e: R_min")
print("g: G_max")
print("f: G_min")
print("b: B_max")
print("v: B_min")
print("p: Change color point plus")
print("c: Change color point cross")
print("u: Canvas upper left")
print("j: Canvas lower left")
print("i: Canvas upper right")
print("Press 'y' to confirm")

confirm = False
while not confirm:
    confirm = input("Are the points correct? (y/n) ") == 'y'
    canvas.print_points()

# Draw the image on the canvas
mouses = dc.mouse.Controller()

dc.draw_image_color(mouses, canvas.get_points(), pixels)
