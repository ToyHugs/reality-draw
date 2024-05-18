import lib.draw_canvas as dc
import lib.select_canvas as sc
import lib.img_import as ii

path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\BNA_PP.png"
# path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\Instagram_icon.png"

# Import the image and decomplexify the color of the image
pixels = ii.import_image(path_img)
pixels = ii.resize_image(pixels, 40)
pixels = ii.color_decomplex(pixels, 4)

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

dc.draw_image(mouses, canvas.get_points(), pixels)
