import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main():
    """Main function to crop/zoom on an image."""
    try:
        # Load the image
        image_path = "animal.jpeg"
        image = ft_load(image_path)
        image_array = np.array(image)

        # Print image information
        print(f"The shape of image is: {image_array.shape}")
        print(image_array[:1])  # Print the first row of pixels

        # Crop the image and convert it to grayscale
        cropped_image_array = image_array[:400, :400, 0]
        grey_image_array = np.mean(cropped_image_array, axis=2,
                                   keepdims=True).astype(np.uint8)
        print(f"New shape after slicing: {grey_image_array.shape} "
              f"or {grey_image_array.shape[:2]}"
              )
        print(grey_image_array[:1])  # Print the first row of cropped pixels

        # Display the cropped image with scales on x and y axes
        plt.imshow(grey_image_array.squeeze(), cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
