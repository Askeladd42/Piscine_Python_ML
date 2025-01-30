import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def transpose_image(array):
    """Manually transpose a 2D array"""
    rows, cols = array.shape
    transposed_array = np.zeros((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed_array[j, i] = array[i, j]
    return transposed_array


def main():
    """Main function to rotate an image."""
    try:
        # Load the image
        image_path = "animal.jpeg"
        image = ft_load(image_path)
        image_array = np.array(image)

        # Cut a square part from the image
        square_image_array = image_array[:400, :400, 0]
        print(f"The shape of image is: {square_image_array.shape}")
        # Print the first row of pixels
        print(square_image_array[:1])

        # Manually transpose the image
        transposed_image_array = transpose_image(square_image_array)
        print(f"New shape after Transpose: {transposed_image_array.shape}")
        # Print the first row of transposed pixels
        print(transposed_image_array[:1])

        # Display the rotated image
        plt.imshow(transposed_image_array, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
