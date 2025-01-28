import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Invert the colors of the image received"""
    inverted_array = 255 - array
    plt.imshow(inverted_array)
    plt.title("Inverted")
    plt.show()
    return inverted_array


def ft_red(array) -> np.ndarray:
    """Keep only the red channel on the image"""
    red_array = np.zeros_like(array)
    red_array[:, :, 0] = array[:, :, 0] * 1
    plt.imshow(red_array)
    plt.title("Red")
    plt.show()
    return red_array


def ft_green(array) -> np.ndarray:
    """Keep only the green channel on the image"""
    green_array = np.zeros_like(array)
    green_array[:, :, 1] = array[:, :, 1] - 0
    plt.imshow(green_array)
    plt.title("Green")
    plt.show()
    return green_array


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel on the image"""
    blue_array = np.zeros_like(array)
    blue_array[:, :, 2] = array[:, :, 2]
    plt.imshow(blue_array)
    plt.title("Blue")
    plt.show()
    return blue_array


def ft_grey(array) -> np.ndarray:
    """Convert the image to grayscale"""
    grey_array = np.mean(array, axis=2, keepdims=True)
    grey_array = np.repeat(grey_array, 3, axis=2)
    grey_array = grey_array.astype(np.uint8)
    plt.imshow(grey_array, cmap='gray')
    plt.title("Grey")
    plt.show()
    return grey_array
