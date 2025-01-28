import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main():
    try:
        # Load the image
        image_path = "animal.jpeg"
        image = ft_load(image_path)
        image_array = np.array(image)

        # Cut a square part from the image
        square_image_array = image_array[:400, :400, :1]
        print(f"The shape of image is: {square_image_array.shape}")
        print(square_image_array[:1])  # Print the first row of pixels

        # Transpose the image
        transposed_image_array = np.transpose(square_image_array.squeeze())
        print(f"New shape after Transpose: {transposed_image_array.shape}")
        # Print the first row of transposed pixels
        print(transposed_image_array[:1])

        # Display the rotated image
        plt.imshow(transposed_image_array, cmap='gray')
        plt.title('Rotated Image')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
