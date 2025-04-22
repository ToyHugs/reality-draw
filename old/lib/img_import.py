# Lib for importing image and manipulate it
# Only png images are supported (alpha channel isn't supported)

from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
from sklearn.cluster import KMeans


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

def color_reductor(pixels: list[list[int]], number_of_colors: int) -> list[list[int]]:
    """
    Reduce the number of colors of the image with 
    """
    # Convert the image to a numpy array for the KMeans
    height, width = len(pixels), len(pixels[0])
    image = np.array([list(pixels[i][j]) for i in range(height) for j in range(width)])  

    # Use KMeans to reduce the number of colors
    kmeans = KMeans(n_clusters=number_of_colors, random_state=0).fit(image)
    new_colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_

    # Replace the colors of the image
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = tuple(new_colors[labels[i * width + j]])

    return pixels

