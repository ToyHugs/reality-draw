import lib.img_import as ii
import matplotlib.pyplot as plt

path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\BNA_PP.png"

def test_import_img():
    pixels = ii.import_image(path_img)
    pixels = ii.resize_image(pixels, 50)
    pixels = ii.color_decomplex(pixels, 4)
    ii.show_image(pixels)
    

test_import_img()
