import lib.img_import as ii
import matplotlib.pyplot as plt

path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\BNA_PP.png"
path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\20240518_072729.jpg"
path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\nanami.jpg"
path_img = "C:\\Users\\xonit\\gitlab\\reality-draw\\src\\gojo.jpg"

def test_import_img():
    pixels = ii.import_image(path_img)
    pixels = ii.resize_image(pixels, 100)
    pixels = ii.color_reductor(pixels, 500)
    ii.show_image(pixels)
    

test_import_img()
