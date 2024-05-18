# Lib for importing image and manipulate it
# Only png images are supported (alpha channel isn't supported)

from PIL import Image
import matplotlib.pyplot as plt

def import_image(path: str) -> Image:
    """
    Return the list of the pixel of the image
    """
    # Open the image and convert it to RGB
    image = Image.open(path)
    image = image.convert('RGB')

    # Resize the image to a square of the smallest size
    if image.width < image.height:
        image = image.resize((image.width, image.width))
    else:
        image = image.resize((image.height, image.height))

    # Get the pixel of the image
    pixels = list(image.getdata())
    pixels = [pixels[i * image.width:(i + 1) * image.width] for i in range(image.height)]

    return pixels

def show_image(pixels: list[list[int]]):
    """
    Show the image
    """
    plt.imshow(pixels)
    plt.show()

def resize_image(pixels: list[list[int]], new_size: int) -> list[list[int]]:
    """
    Resize the image to a new size
    """
    image = Image.new('RGB', (len(pixels), len(pixels)))
    image.putdata([pixel for line in pixels for pixel in line])    
    image = image.resize((new_size, new_size))

    pixels = list(image.getdata())
    pixels = [pixels[i * new_size:(i + 1) * new_size] for i in range(new_size)]

    return pixels

def color_decomplex(pixels: list[list[int]], bits: int) -> list[list[int]]:
    """
    De-complexify the color of the image
    """
    assert 0 <= bits <= 8

    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            new_pixel = []
            for k in range(3):
                new_pixel.append(int(pixels[i][j][k] >> bits) * 2 ** bits)

            pixels[i][j] = tuple(new_pixel)

    return pixels